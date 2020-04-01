import unittest
# import conf
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult
import exceptions
import shutil
import os


class TestGxx(unittest.TestCase):
    submission_lang = "GXX"
    submission_dir = f'problems/1/test'

    def test_AC(self):
        self.submission_dir = f'problems/1/test'
        ac_code = """
        #include <iostream>
        using namespace std;
        int main() {
            int a, b;
            cin >> a >> b;
            cout << a + b<< endl;
            return 0;
        }
        """
        submitted_executor = get_executor("GXX", ac_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 100072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)

        self.assertEqual(result['verdict'], VerdictResult.AC)

    def test_WA(self):
        self.submission_dir = f'problems/1/test'
        wa_code = """
            #include <iostream>
            using namespace std;
            int main() {
                int a, b;
                cin >> a >> b;
                cout << a + b + 2 << endl;
                return 0;
            }
        """
        submitted_executor = get_executor("GXX", wa_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 131072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])

        self.assertEqual(result['verdict'], VerdictResult.WA)

    def test_TLE(self):
        self.submission_dir = f'problems/1/test'
        tle_code = """
            #include <iostream>
            using namespace std;
            int main() {
                int a, b;
                cin >> a >> b;
                while(true){
                    a += b;
                }
                cout << a + b << endl;
                return 0;
            }
        """
        submitted_executor = get_executor(self.submission_lang, tle_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1111,
            "memory_limit": 131072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])

        self.assertEqual(result["verdict"], VerdictResult.TLE)

    def test_MLE(self):
        self.submission_dir = f'problems/1/test'
        mle_code = """
            #include <iostream>
            int fuck[3000000];
            int dick[3000000];
            using namespace std;
            int main() {
                int a, b;
                cin >> a >> b;
                for(int i = 0;i < 3000000;i++)
                { fuck[i] = i;
                dick[i] = i;}
                cout << a + b << endl;
                return 0;
            }
        """
        submitted_executor = get_executor(self.submission_lang, mle_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 10011,
            "memory_limit": 26072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])

        self.assertEqual(result["verdict"], VerdictResult.MLE)

    def test_RE(self):
        self.submission_dir = f'problems/1/test'
        re_code = """
            #include <iostream>
            int fuck[60000];
            using namespace std;
            int main() {
                int a, b;
                cin >> a >> b;
                for(int i = 0;i < 65000;i++)
                { fuck[i] = i;
                }
                cout << a + b << endl;
                return 0;
            }
        """
        submitted_executor = get_executor(self.submission_lang, re_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1111,
            "memory_limit": 306072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])

        self.assertEqual(result["verdict"], VerdictResult.RE)

    def test_CE(self):
        self.submission_dir = f'problems/1/test'
        ce_code = """
            #include <iostream>
            int fuck[60000000000];
            using namespace std;
            int main() {
                int a, b;
                cin >> a >> b;
                for(int i = 0;i < 60050000000;i++)
                { fuck[i] = i;
               }
                cout << a + b << endl;
                return 0;
            }
        """
        with self.assertRaises(exceptions.ExecutorInitException) as cm:
            submitted_executor = get_executor(self.submission_lang, ce_code, f'{self.submission_dir}/submitted')
            print(cm.exception)

    def test_OLE(self):
        self.submission_dir = f'problems/1/test'
        ole_code = """
                    #include <stdio.h>
                    int main() {
                        int a, b;
                        scanf("%d%d",&a,&b);
                        for(int i = 0;i < 20000000;i++)
                            printf("%d",a);

                        return 0;
                    }
                """
        submitted_executor = get_executor(self.submission_lang, ole_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 22222,
            "memory_limit": 306072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])

        self.assertEqual(result["verdict"], VerdictResult.OLE)

    def tearDown(self) -> None:
        shutil.rmtree(self.submission_dir, ignore_errors=True)
