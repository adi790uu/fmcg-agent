from src.services.product_service import ProductService
from src.core.mock_data import products_mock_data
import pytest_asyncio
import pytest


@pytest_asyncio.fixture
async def product_service():
    service = ProductService()
    return service


@pytest.mark.asyncio
async def test_get_all_product_info(product_service):
    products = await product_service.get_all_products_info()
    assert products == products_mock_data


@pytest.mark.asyncio
async def test_get_product_info(product_service):
    product_name_list = ["Hair Oil", "haIr OIl", "xyz"]

    expected = [
        True,
        True,
        False,
    ]
    for product_name, expected in zip(product_name_list, expected):
        product_info = await product_service.get_product_info(product_name)
        assert (product_info is not None) == expected


@pytest.mark.asyncio
async def test_get_product_stock(product_service):
    product_name_list = ["Hair Oil", "haIr OIl", "xyz"]

    expected = [
        True,
        True,
        False,
    ]

    for product_name, expected in zip(product_name_list, expected):
        product_stock = await product_service.get_product_stock(product_name)
        assert (product_stock is not None) == expected
