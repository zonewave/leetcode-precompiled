import json

py = """
from precompiled.all import *
@dataclass
class Args:
    $1: $2 
    $3: $4
    // add


@dataclass
class LTestCase:
    name: str
    args: Args
    want: $5  # replace


class TestSolution(TestCase):
    # replace name
    def test_$6(self):
        cases: list[LTestCase] = [
            # add args
            LTestCase("1", Args(), ),
            # LTestCase("2", Args(), ),
            # LTestCase("3", Args(), ),
        ]
        s = Solution()
        for case in cases:
            with self.subTest(case=case.name):
                # may be replace func name
                self.assertEqual(s.$6(**case.args.__dict__), case.want)
"""

cpp = """
struct Args {
    mutable ? ;
    mutable ? ;
};

struct LTestCase {
    string name;
    Args args;
    ? want;
};

TEST_CASE("test cases") {
    Solution s;

    vector<LTestCase> cases = {
        // todo
        {"1", {}, },
    };

    for (const auto& case_ : cases) {
        SUBCASE(case_.name.c_str()) {
            vector<int> result = s.?(case_.args.arg1, case_.args.arg2);
            CHECK(result == case_.want); 
        }
    }
}
"""


def print_json(tmpl):
    code_lines = tmpl.split("\n")
    code_json = json.dumps(code_lines)
    print(code_json)


if __name__ == '__main__':
    # print(py)
    print_json(cpp)
