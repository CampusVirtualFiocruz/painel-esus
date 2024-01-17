import pytest
from src.data.interfaces.create_bases.create_bases_repository import \
    CreateBasesRepositoryInterface
from src.data.use_cases.create_bases.create_bases_usecase import \
    CreateBasesUseCase
from src.errors import InvalidArgument


def test_create_base_use_case_no_base():
    with pytest.raises(InvalidArgument) as exc:
        usecase = CreateBasesUseCase()
        usecase.create_bases()
        assert exc.message == 'No bases to generate was passed.'


def test_create_base_use_case_no_compatible_args():
    _list = [12, 23]
    with pytest.raises(InvalidArgument) as exc:
        usecase = CreateBasesUseCase(_list)
        usecase.create_bases()
        assert exc.message == 'Base is no instance of CreateBasesRepositoryInterface.'

        _list = ['12', '23']
    with pytest.raises(InvalidArgument) as exc:
        usecase = CreateBasesUseCase(_list)
        usecase.create_bases()
        assert exc.message == 'Base is no instance of CreateBasesRepositoryInterface.'


def test_create_base_use_case():

    class CreateBaseStub(CreateBasesRepositoryInterface):
        def create_base(self):
            print('ok created')

        def destroy_base(self):
            print('ok destroyed')
    _list = [
        CreateBaseStub()
    ]
    try:
        usecase = CreateBasesUseCase(_list)
        usecase.create_bases()
    except Exception:
        assert False
