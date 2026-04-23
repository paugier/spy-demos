format:
	ruff format *.spy *.py


rs_lazy:
	spy rs lazy_add.spy --dump lib_array1d.spy | ./simplify_rs_output.py

rs_lazysin:
	spy rs lazy_add_sin.spy --dump lib_ndarray.spy | ./simplify_rs_output.py

rs_simple:
	spy rs simple_loop.spy --dump lib_array1d_simple.spy | ./simplify_rs_output.py


rs_liblazy:
	spy rs lib_array1d.spy | ./simplify_rs_output.py

rs_liblazysin:
	spy rs lib_ndarray.spy | ./simplify_rs_output.py

rs_libsimple:
	spy rs lib_array1d_simple.spy | ./simplify_rs_output.py


test_lazy:
	spy lazy_add.spy

test_lazysin:
	spy lazy_add_sin.spy

test_simple:
	spy simple_loop.spy

test_build_lazy:
	spy build -x lazy_add.spy

test_build_lazysin:
	spy build -x lazy_add_sin.spy

test_build_simple:
	spy build -x simple_loop.spy

test: test_lazy test_lazysin test_simple test_build_lazy test_build_lazysin test_build_simple


rs_lazysimple:
	spy rs lazy_simple.spy | ./simplify_rs_output.py

rs_lazysimple_noinline:
	spy rs --no-inline lazy_simple.spy | ./simplify_rs_output.py
