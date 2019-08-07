from monkey_patch import original_code


class MonkeyPatchTest:

    def method_a(self):
        print('New code implementation')

    def test_monkey_patch(self):
        original_code.MonkeyPatch.method_a = self.method_a
        m_obj = original_code.MonkeyPatch()
        m_obj.method_a()


m = MonkeyPatchTest()
m.test_monkey_patch()  # New code implementation
