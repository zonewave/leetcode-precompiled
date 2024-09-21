# LeetCode Local Debugging Environment Configuration (JetBrains)

[中文文档](https://github.com/zonewave/leetcode-precomiled/blob/master/README_CN.md)
## Introduction

This project is based on leetcode-editor and provides problem solution templates to facilitate local debugging of LeetCode environments.

## Motivation
Solving problems on the web can be quite painful, especially when encountering complex test cases that fail to pass. It often takes a long time to pinpoint the issues. Therefore, I wanted to use a local IDE for step-by-step debugging of LeetCode problems, as it's generally more convenient and allows for quicker issue identification. I later installed leetcode-editor in PyCharm. However, the default templates were too simplistic, making it cumbersome to write test cases, and I couldn't find good templates online. This led to the creation of this project. With my template, you only need to configure the parameter types, and then you can simply copy the test cases from the problem description to run them. Currently, it only supports Python, but there will be support for other languages in the future.

### [Python](https://github.com/zonewave/leetcode-precomiled/blob/master/py/README.md)
![debug](https://github.com/zonewave/leetcode-precomiled/blob/master/py/img/debug.jpg)

## Features

- Supports multiple programming languages with toolkits, including all officially declared data structures such as `ListNode`, `NestedInteger`, `TreeNode`, etc.
- Provides some utility functions for better local testing.
- Based on leetcode-editor, offers template content for various programming languages.
- Easy to use, suitable for quickly configuring a local debugging environment for LeetCode problems.

## Supported Programming Languages

- [x] [Python](./py/README.md)
- [ ] Go
- [ ] Java
- [ ] CSharp
- [ ] C++
- [ ] C
- [ ] Rust

## Contributions

Contributions of any kind are welcome! If you have new data structures or suggestions for improvements, please submit a pull request or raise an issue.

## License

This project is licensed under the MIT License. For more details, please see the [LICENSE](https://github.com/zonewave/leetcode-precomiled/blob/master/LICENSE) file.

## Contact Information

If you have any questions, please contact the project maintainer.