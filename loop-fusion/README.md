# Demo about array loop fusion with SPy

This demo uses the branch https://github.com/paugier/spy/tree/generic-class (but this is a detail
since this branch is just about syntactic sugar).

- lazy_add.spy is a minimal example (only 1d and only `__add__`)
- lazy_add_sin.spy is a more advanced example with 1d and 2d ndarray, `__add__` and `sin`

To see what happens, run

```sh
spy rs lazy_add.spy -> result.spy
./simplify_rs_output.py result.spy
```

There is just one loop per array expression (for example `out1: ndarray[f64] = x + x + x`).

Note that SPy fails to build this files.

There are of course many things that could be improved to be able to do that with nicer code, in particular:

- `type A = ndarray[DTYPE, NDIM]` syntax and `__blue_checks__` (https://github.com/spylang/spy/pull/448#issuecomment-4199438746)

- `unroll` for blue loops

- Fix bug `assert w_func.w_functype.kind != "metafunc"` (see comments lazy_add_sin.spy)

- Avoid `def shape(self) -> gc_ptr[i32]`

- Get `DTYPE` and `NDIM` (blue values) from `T=ndarray[DTYPE, NDIM]`?
