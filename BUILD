py_library(
    name = "lib",
    srcs = [
        "lib.py",
    ],
    srcs_version = "PY2",
)

py_test(
    name = "test",
    srcs = ["test.py"],
    python_version = "PY2",
    srcs_version = "PY2",
    deps = [":lib"],
)
