import py, sys
from testing import backend_tests
from cffibuilder.backend_ctypes import CTypesBackend


class TestCTypes(backend_tests.BackendTests):
    # for individual tests see
    # ====> backend_tests.py
    
    Backend = CTypesBackend
    TypeRepr = "<class 'ffi.CData<%s>'>"

    def test_array_of_func_ptr(self):
        py.test.skip("ctypes backend: not supported: "
                     "initializers for function pointers")

    def test_structptr_argument(self):
        py.test.skip("ctypes backend: not supported: passing a list "
                     "for a pointer argument")

    def test_array_argument_as_list(self):
        py.test.skip("ctypes backend: not supported: passing a list "
                     "for a pointer argument")

    def test_cast_to_array_type(self):
        py.test.skip("ctypes backend: not supported: casting to array")

    def test_nested_anonymous_struct(self):
        py.test.skip("ctypes backend: not supported: nested anonymous struct")

    def test_nested_anonymous_union(self):
        py.test.skip("ctypes backend: not supported: nested anonymous union")

    def test_CData_CType_2(self):
        if sys.version_info >= (3,):
            py.test.skip("ctypes backend: not supported in Python 3: CType")
        backend_tests.BackendTests.test_CData_CType_2(self)