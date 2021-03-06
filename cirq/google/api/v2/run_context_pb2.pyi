# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import google.protobuf.internal.containers
import google.protobuf.message
import typing

class RunContext(google.protobuf.message.Message):

    @property
    def parameter_sweeps(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ParameterSweep]: ...

    def __init__(self,
        parameter_sweeps : typing.Optional[typing.Iterable[ParameterSweep]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RunContext: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...

class ParameterSweep(google.protobuf.message.Message):
    repetitions = ... # type: int

    @property
    def sweep(self) -> Sweep: ...

    def __init__(self,
        repetitions : typing.Optional[int] = None,
        sweep : typing.Optional[Sweep] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ParameterSweep: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...

class Sweep(google.protobuf.message.Message):

    @property
    def sweep_function(self) -> SweepFunction: ...

    @property
    def single_sweep(self) -> SingleSweep: ...

    def __init__(self,
        sweep_function : typing.Optional[SweepFunction] = None,
        single_sweep : typing.Optional[SingleSweep] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Sweep: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...

class SweepFunction(google.protobuf.message.Message):
    class FunctionType(int):
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> int: ...
        @classmethod
        def keys(cls) -> typing.List[str]: ...
        @classmethod
        def values(cls) -> typing.List[int]: ...
        @classmethod
        def items(cls) -> typing.List[typing.Tuple[str, int]]: ...
    FUNCTION_TYPE_UNSPECIFIED = typing.cast(FunctionType, 0)
    PRODUCT = typing.cast(FunctionType, 1)
    ZIP = typing.cast(FunctionType, 2)

    function_type = ... # type: SweepFunction.FunctionType

    @property
    def sweeps(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[Sweep]: ...

    def __init__(self,
        function_type : typing.Optional[SweepFunction.FunctionType] = None,
        sweeps : typing.Optional[typing.Iterable[Sweep]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SweepFunction: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...

class SingleSweep(google.protobuf.message.Message):
    parameter_key = ... # type: typing.Text

    @property
    def points(self) -> Points: ...

    @property
    def linspace(self) -> Linspace: ...

    def __init__(self,
        parameter_key : typing.Optional[typing.Text] = None,
        points : typing.Optional[Points] = None,
        linspace : typing.Optional[Linspace] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SingleSweep: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...

class Points(google.protobuf.message.Message):
    points = ... # type: google.protobuf.internal.containers.RepeatedScalarFieldContainer[float]

    def __init__(self,
        points : typing.Optional[typing.Iterable[float]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Points: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...

class Linspace(google.protobuf.message.Message):
    first_point = ... # type: float
    last_point = ... # type: float
    num_points = ... # type: int

    def __init__(self,
        first_point : typing.Optional[float] = None,
        last_point : typing.Optional[float] = None,
        num_points : typing.Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Linspace: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
