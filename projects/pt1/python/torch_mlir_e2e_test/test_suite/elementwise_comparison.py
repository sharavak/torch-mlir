# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Also available under a BSD-style license. See LICENSE.

import torch

from torch_mlir_e2e_test.framework import TestUtils
from torch_mlir_e2e_test.registry import register_test_case
from torch_mlir_e2e_test.annotations import annotate_args, export

# ==============================================================================


class ElementwiseGtFloatScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
        ]
    )
    def forward(self, x):
        return torch.gt(x, 0.6)


@register_test_case(module_factory=lambda: ElementwiseGtFloatScalarModule())
def ElementwiseGtFloatScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5))


# ==============================================================================


class ElementwiseGtIntScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
        ]
    )
    def forward(self, x):
        return torch.gt(x, 10)


@register_test_case(module_factory=lambda: ElementwiseGtIntScalarModule())
def ElementwiseGtIntScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 4, low=-10, high=15))


# ==============================================================================


class ElementwiseGtMixed2ScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int32, True),
        ]
    )
    def forward(self, x):
        return torch.gt(x, 7)


@register_test_case(module_factory=lambda: ElementwiseGtMixed2ScalarModule())
def ElementwiseGtMixed2ScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 4, low=-10, high=15).to(torch.int32))


# ==============================================================================


class ElementwiseGeFloatScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
        ]
    )
    def forward(self, x):
        return torch.ge(x, 0.6)


@register_test_case(module_factory=lambda: ElementwiseGeFloatScalarModule())
def ElementwiseGeFloatScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5))


# ==============================================================================


class ElementwiseGeIntScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
        ]
    )
    def forward(self, x):
        return torch.ge(x, 10)


@register_test_case(module_factory=lambda: ElementwiseGeIntScalarModule())
def ElementwiseGeIntScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 4, low=-10, high=15))


# ==============================================================================


class ElementwiseGeMixedIntScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int32, True),
        ]
    )
    def forward(self, x):
        return torch.ge(x, 7)


@register_test_case(module_factory=lambda: ElementwiseGeMixedIntScalarModule())
def ElementwiseGeMixedIntScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 4, low=-10, high=15).to(torch.int32))


# ==============================================================================


class ElementwiseGeFloatIntScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
        ]
    )
    def forward(self, x):
        return torch.ge(x, 7)


@register_test_case(module_factory=lambda: ElementwiseGeFloatIntScalarModule())
def ElementwiseGeFloatIntScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5))


# ==============================================================================


class ElementwiseGeFloatTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
            ([-1], torch.float32, True),
        ]
    )
    def forward(self, x, y):
        return torch.ge(x, y)


@register_test_case(module_factory=lambda: ElementwiseGeFloatTensorModule())
def ElementwiseGeFloatTensorModule_basic(module, tu: TestUtils):
    module.forward(
        torch.tensor([[1.0, 2.2, torch.nan], [6.0, 2.0, 3.1]]).to(torch.float32),
        torch.tensor([6.0, 2.1, torch.nan]).to(torch.float32),
    )


# ==============================================================================


class ElementwiseGeIntTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
            ([-1], torch.int64, True),
        ]
    )
    def forward(self, x, y):
        return torch.ge(x, y)


@register_test_case(module_factory=lambda: ElementwiseGeIntTensorModule())
def ElementwiseGeIntTensorModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 5, high=10), tu.randint(5, high=10))


# ==============================================================================


class ElementwiseGtFloatTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
            ([-1], torch.float32, True),
        ]
    )
    def forward(self, x, y):
        return torch.gt(x, y)


@register_test_case(module_factory=lambda: ElementwiseGtFloatTensorModule())
def ElementwiseGtFloatTensorModule_basic(module, tu: TestUtils):
    module.forward(
        torch.tensor([[1.0, 2.2, torch.nan], [6.0, 2.0, 3.1]]).to(torch.float32),
        torch.tensor([6.0, 2.1, torch.nan]).to(torch.float32),
    )


# ==============================================================================


class ElementwiseGtIntTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
            ([-1], torch.int64, True),
        ]
    )
    def forward(self, x, y):
        return torch.gt(x, y)


@register_test_case(module_factory=lambda: ElementwiseGtIntTensorModule())
def ElementwiseGtIntTensorModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 5, high=10), tu.randint(5, high=10))


# ==============================================================================


class ElementwiseLtFloatScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
        ]
    )
    def forward(self, x):
        return torch.lt(x, 0.6)


@register_test_case(module_factory=lambda: ElementwiseLtFloatScalarModule())
def ElementwiseLtFloatScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5))


# ==============================================================================


class ElementwiseHeavisideModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([5], torch.float32, True), ([1], torch.float32, True)])
    def forward(self, x, values):
        return torch.heaviside(x, values)


@register_test_case(module_factory=lambda: ElementwiseHeavisideModule())
def ElementwiseHeavisideModule_basic(module, tu: TestUtils):
    module.forward(
        torch.tensor([1.0, -2.0, torch.inf, torch.nan, -torch.inf]), torch.tensor([5.0])
    )


class ElementwiseHeavisideIntModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [None, ([-1, -1, -1], torch.int64, True), ([-1, -1, -1, -1], torch.int64, True)]
    )
    def forward(self, x, values):
        return torch.heaviside(x, values)


@register_test_case(module_factory=lambda: ElementwiseHeavisideIntModule())
def ElementwiseHeavisideIntModule_basic(module, tu: TestUtils):
    module.forward(
        tu.randint(1, 2, 3, low=-100, high=1000),
        tu.randint(1, 1, 1, 1, low=-100, high=1000),
    )


class ElementwiseHeavisideNoBroadcastModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [None, ([-1, -1], torch.float32, True), ([-1, -1], torch.float32, True)]
    )
    def forward(self, x, values):
        return torch.heaviside(x, values)


@register_test_case(module_factory=lambda: ElementwiseHeavisideNoBroadcastModule())
def ElementwiseHeavisideNoBroadcastModule_basic(module, tu: TestUtils):
    module.forward(
        tu.rand(5, 8),
        tu.rand(5, 8),
    )


# ==============================================================================


class ElementwiseLtIntScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
        ]
    )
    def forward(self, x):
        return torch.lt(x, 0)


@register_test_case(module_factory=lambda: ElementwiseLtIntScalarModule())
def ElementwiseLtIntScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 4, low=-10, high=15))


class ElementwiseIntTensorLtFloatScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1], torch.int64, True),
        ]
    )
    def forward(self, x):
        return torch.lt(x, 1.1)


@register_test_case(module_factory=lambda: ElementwiseIntTensorLtFloatScalarModule())
def ElementwiseIntTensorLtFloatScalarModule_basic(module, tu: TestUtils):
    module.forward(torch.tensor([0, 1, 2, 3], dtype=torch.int64))


class ElementwiseFloatTensorGtIntScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1], torch.float32, True),
        ]
    )
    def forward(self, x):
        return torch.gt(x, 1)


@register_test_case(module_factory=lambda: ElementwiseFloatTensorGtIntScalarModule())
def ElementwiseFloatTensorGtIntScalarModule_basic(module, tu: TestUtils):
    module.forward(torch.tensor([0.9, 1.1, 2.0, 3.0], dtype=torch.float32))


# ==============================================================================


class ElementwiseLtDiffWidthScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int32, True),
        ]
    )
    def forward(self, x):
        return torch.lt(x, 2)


@register_test_case(module_factory=lambda: ElementwiseLtDiffWidthScalarModule())
def ElementwiseLtDiffWidthScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 4, low=-10, high=15).to(torch.int32))


# ==============================================================================


class ElementwiseLeFloatScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
        ]
    )
    def forward(self, x):
        return torch.le(x, 0.6)


@register_test_case(module_factory=lambda: ElementwiseLeFloatScalarModule())
def ElementwiseLeFloatScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5))


# ==============================================================================


class ElementwiseLeIntScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
        ]
    )
    def forward(self, x):
        return torch.le(x, 10)


@register_test_case(module_factory=lambda: ElementwiseLeIntScalarModule())
def ElementwiseLeIntScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 4, low=-10, high=15))


# ==============================================================================


class ElementwiseLeMixedIntScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int32, True),
        ]
    )
    def forward(self, x):
        return torch.le(x, 7)


@register_test_case(module_factory=lambda: ElementwiseLeMixedIntScalarModule())
def ElementwiseLeMixedIntScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 4, low=-10, high=15).to(torch.int32))


# ==============================================================================


class ElementwiseLeFloatIntScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
        ]
    )
    def forward(self, x):
        return torch.le(x, 7)


@register_test_case(module_factory=lambda: ElementwiseLeFloatIntScalarModule())
def ElementwiseLeFloatIntScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5))


# ==============================================================================


class ElementwiseLeFloatTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
            ([-1], torch.float32, True),
        ]
    )
    def forward(self, x, y):
        return torch.le(x, y)


@register_test_case(module_factory=lambda: ElementwiseLeFloatTensorModule())
def ElementwiseLeFloatTensorModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5), tu.rand(5))


# ==============================================================================


class ElementwiseLeFloatTensorNanModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
            ([-1], torch.float32, True),
        ]
    )
    def forward(self, x, y):
        return torch.le(x, y)


@register_test_case(module_factory=lambda: ElementwiseLeFloatTensorNanModule())
def ElementwiseLeFloatTensorNanModule_basic(module, tu: TestUtils):
    module.forward(
        torch.tensor([[1.0, 2.2, torch.nan], [6.0, 2.0, 3.1]]).to(torch.float32),
        torch.tensor([6.0, 2.1, torch.nan]).to(torch.float32),
    )


# ==============================================================================


class ElementwiseLeIntTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
            ([-1], torch.int64, True),
        ]
    )
    def forward(self, x, y):
        return torch.le(x, y)


@register_test_case(module_factory=lambda: ElementwiseLeIntTensorModule())
def ElementwiseLeIntTensorModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 5, high=10), tu.randint(5, high=10))


# ==============================================================================


class ElementwiseLtFloatTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
            ([-1], torch.float32, True),
        ]
    )
    def forward(self, x, y):
        return torch.lt(x, y)


@register_test_case(module_factory=lambda: ElementwiseLtFloatTensorModule())
def ElementwiseLtFloatTensorModule_basic(module, tu: TestUtils):
    module.forward(
        torch.tensor([[1.0, 2.2, torch.nan], [6.0, 2.0, 3.1]]).to(torch.float32),
        torch.tensor([6.0, 2.1, torch.nan]).to(torch.float32),
    )


# ==============================================================================


class ElementwiseLtIntTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
            ([-1], torch.int64, True),
        ]
    )
    def forward(self, x, y):
        return torch.lt(x, y)


@register_test_case(module_factory=lambda: ElementwiseLtIntTensorModule())
def ElementwiseLtIntTensorModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 5, high=10), tu.randint(5, high=10))


class ElementwiseIntTensorLtFloatTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
            ([-1], torch.float64, True),
        ]
    )
    def forward(self, x, y):
        return torch.lt(x, y)


@register_test_case(module_factory=lambda: ElementwiseIntTensorLtFloatTensorModule())
def ElementwiseIntTensorLtFloatTensorModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 5, high=10), tu.rand(5, high=10).to(torch.float64))


class ElementwiseFloatTensorGtIntTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
            ([-1], torch.int32, True),
        ]
    )
    def forward(self, x, y):
        return torch.gt(x, y)


@register_test_case(module_factory=lambda: ElementwiseIntTensorLtFloatTensorModule())
def ElementwiseFloatTensorGtIntTensorModule_basic(module, tu: TestUtils):
    module.forward(
        tu.rand(3, 5, high=10).to(torch.float32),
        tu.randint(5, high=10, dtype=torch.int32),
    )


# ==============================================================================


class ElementwiseEqFloatScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
        ]
    )
    def forward(self, x):
        return torch.eq(x, 6.0)


@register_test_case(module_factory=lambda: ElementwiseEqFloatScalarModule())
def ElementwiseEqFloatScalarModule_basic(module, tu: TestUtils):
    module.forward(
        torch.tensor([[1.0, 2.2, torch.nan], [6.0, 2.0, 3.1]]).to(torch.float32)
    )


# ==============================================================================


class ElementwiseEqIntScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
        ]
    )
    def forward(self, x):
        return torch.eq(x, 2)


@register_test_case(module_factory=lambda: ElementwiseEqIntScalarModule())
def ElementwiseEqIntScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(5, 8, low=2, high=4))


# ==============================================================================


class ElementwiseEqBoolScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.bool, True),
        ]
    )
    def forward(self, x):
        return torch.eq(x, 1)


@register_test_case(module_factory=lambda: ElementwiseEqBoolScalarModule())
def ElementwiseEqBoolScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 4, low=0, high=1, dtype=torch.bool))


# ==============================================================================


class ElementwiseEqDiffWidthScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int32, True),
        ]
    )
    def forward(self, x):
        return torch.eq(x, 2)


@register_test_case(module_factory=lambda: ElementwiseEqDiffWidthScalarModule())
def ElementwiseEqDiffWidthScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(5, 8, low=2, high=4).to(torch.int32))


# ==============================================================================


class ElementwiseEqFloatTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
            ([-1], torch.float32, True),
        ]
    )
    def forward(self, x, y):
        return torch.eq(x, y)


@register_test_case(module_factory=lambda: ElementwiseEqFloatTensorModule())
def ElementwiseEqFloatTensorModule_basic(module, tu: TestUtils):
    module.forward(
        torch.tensor([[1.0, 2.2, 6.0], [torch.nan, 2.0, 3.1]]).to(torch.float32),
        torch.tensor([1.0, 2.4, 6.0]).to(torch.float32),
    )


# ==============================================================================


class ElementwiseEqIntTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
            ([-1], torch.int64, True),
        ]
    )
    def forward(self, x, y):
        return torch.eq(x, y)


@register_test_case(module_factory=lambda: ElementwiseEqIntTensorModule())
def ElementwiseEqIntTensorModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(8, 5, low=2, high=4), tu.randint(5, low=2, high=4))


# ==============================================================================


class ElementwiseNeFloatScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
        ]
    )
    def forward(self, x):
        return torch.ne(x, 2.0)


@register_test_case(module_factory=lambda: ElementwiseNeFloatScalarModule())
def ElementwiseNeFloatScalarModule_basic(module, tu: TestUtils):
    module.forward(
        torch.tensor([[1.0, 2.2, 2.0], [torch.nan, 2.0, 3.1]]).to(torch.float32)
    )


# ==============================================================================


class ElementwiseNeIntScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
        ]
    )
    def forward(self, x):
        return torch.ne(x, 3)


@register_test_case(module_factory=lambda: ElementwiseNeIntScalarModule())
def ElementwiseNeIntScalarModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(8, 5, low=2, high=4))


# ==============================================================================


class ElementwiseNeFloatTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
            ([-1, -1], torch.float32, True),
        ]
    )
    def forward(self, x, y):
        return torch.ne(x, y)


@register_test_case(module_factory=lambda: ElementwiseNeFloatTensorModule())
def ElementwiseNeFloatTensorModule_basic(module, tu: TestUtils):
    module.forward(
        torch.tensor([[1.0, 2.2, 6.0], [6.0, 2.0, 3.1]]).to(torch.float32),
        torch.tensor([[1.0, 2.4, 6.0], [torch.nan, 2.0, 6.0]]).to(torch.float32),
    )


# ==============================================================================


class ElementwiseNeIntTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int64, True),
            ([-1], torch.int64, True),
        ]
    )
    def forward(self, x, y):
        return torch.ne(x, y)


@register_test_case(module_factory=lambda: ElementwiseNeIntTensorModule())
def ElementwiseNeIntTensorModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(8, 5, low=2, high=4), tu.randint(5, low=2, high=4))


# ==============================================================================


class ElementwiseNeFloatTensorStaticModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([2, 3], torch.float32, True),
            ([2, 3], torch.float32, True),
        ]
    )
    def forward(self, x, y):
        return torch.ne(x, y)


@register_test_case(module_factory=lambda: ElementwiseNeFloatTensorStaticModule())
def ElementwiseNeFloatTensorStaticModule_basic(module, tu: TestUtils):
    module.forward(
        torch.tensor([[1.0, 2.2, 6.0], [6.0, 2.0, 3.1]]).to(torch.float32),
        torch.tensor([[1.0, 2.4, 6.0], [torch.nan, 2.0, 6.0]]).to(torch.float32),
    )


# ==============================================================================


class ElementwiseNeIntTensorStaticModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([8, 5], torch.int64, True),
            ([5], torch.int64, True),
        ]
    )
    def forward(self, x, y):
        return torch.ne(x, y)


@register_test_case(module_factory=lambda: ElementwiseNeIntTensorStaticModule())
def ElementwiseNeIntTensorStaticModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(8, 5, low=2, high=4), tu.randint(5, low=2, high=4))


# ==============================================================================


class AnyBoolTrueModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
        ]
    )
    def forward(self):
        input = [False, False, True]
        return torch.ops.aten.any(input)


@register_test_case(module_factory=lambda: AnyBoolTrueModule())
def AnyBoolTrueModule_basic(module, tu: TestUtils):
    module.forward()


class AnyBoolFalseModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
        ]
    )
    def forward(self):
        input = [False, False, False]
        return torch.ops.aten.any(input)


@register_test_case(module_factory=lambda: AnyBoolFalseModule())
def AnyBoolFalseModule_basic(module, tu: TestUtils):
    module.forward()


# =================================================================================


class AllBoolTrueModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
        ]
    )
    def forward(self):
        input = [True, True, True, True, True]
        return torch.ops.aten.all(input)


@register_test_case(module_factory=lambda: AllBoolTrueModule())
def AllBoolTrueModule_basic(module, tu: TestUtils):
    module.forward()


# =================================================================================


class AllBoolFalseModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
        ]
    )
    def forward(self):
        input = [True, False, True, True, False]
        return torch.ops.aten.all(input)


@register_test_case(module_factory=lambda: AllBoolFalseModule())
def AllBoolFalseModule_basic(module, tu: TestUtils):
    module.forward()


# ==============================================================================


class ElementwiseIsnanModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1], torch.float32, True),
        ]
    )
    def forward(self, x):
        return torch.ops.aten.isnan(x)


@register_test_case(module_factory=lambda: ElementwiseIsnanModule())
def ElementwiseIsnanModule_basic(module, tu: TestUtils):
    x = torch.tensor([1.0, torch.nan, torch.inf, -torch.inf])
    module.forward(x)


# ==============================================================================


class ElementwiseIsinfModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1], torch.float32, True),
        ]
    )
    def forward(self, x):
        return torch.ops.aten.isinf(x)


@register_test_case(module_factory=lambda: ElementwiseIsinfModule())
def ElementwiseIsinfModule_basic(module, tu: TestUtils):
    x = torch.tensor([1.0, torch.nan, torch.inf, -torch.inf])
    module.forward(x)
