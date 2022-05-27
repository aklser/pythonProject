import unittest


class TestStringMethods(unittest.TestCase):

    # def setUpClass(self) -> None:
    #     pass
    #
    # def tearDownClass(self) -> None:
    #     pass

    def setUp(self) -> None:
        print("开始执行用例！")

    @unittest.skip("用例1跳过了")
    def test_upper(self):
        try:
            self.assertEqual('foo'.upper(), 'FOO')
        except AssertionError:
            print("1有错")
        else:
            print("用例1通过！")

    def test_isupper(self):
        try:
            self.assertEqual("FOO".isupper(), True)
            self.assertTrue("FOO".isupper())
            self.assertFalse("foo".isupper())
        except AssertionError:
            print("2有错")
        else:
            print("用例2通过！")

    def test_split(self):
        s = 'hello world'
        try:
            self.assertEqual(s.split(), ['hello', 'world'])
            with self.assertRaises(TypeError):
                s.split(2)
        except AssertionError:
            print("3有错")
        else:
            print("用例3通过！")

    def test_4(self):
        for i in range(0, 6):
            with self.subTest():
                try:
                    self.assertEqual(i % 2, 0)
                except:
                    print("用例4的第", str(i + 1), "条，有错")
                else:
                    print("用例4的第", str(i + 1), "条，通过")

    def tearDown(self) -> None:
        print("用例结束！")


if __name__ == "__main__":
    unittest.main()
