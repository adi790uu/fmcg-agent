from src.services.order_service import OrderService
import pytest_asyncio
import pytest


@pytest_asyncio.fixture
async def order_service():
    service = OrderService()
    return service


@pytest.mark.asyncio
async def test_add_products_to_cart(order_service):
    add_product_list = [
        "{'Hair Oil': 1, 'Green Tea': 1}",
        "{'HAir oil': 1}",
        "Hair Oil: 1",
        "Hair Oil",
    ]

    expected_results = [True, True, False, False]

    for order_list, expected in zip(add_product_list, expected_results):
        result = await order_service.add_products_to_cart(
            product_name_list=order_list,
        )
        assert result[0] is expected


@pytest.mark.asyncio
async def test_remove_products_from_cart(order_service):
    remove_product_list = [
        "Hair Oil",
        "Hair Oil, Green Tea",
        "hair OiL",
        "{'Hair Oil', 'Green Tea'}",
    ]

    expected = [True, True, True, False]

    for product_list, expected in zip(remove_product_list, expected):
        await order_service.add_products_to_cart(
            product_name_list="{'Hair Oil': 1, 'Green Tea': 1}",
        )
        result = await order_service.remove_products_from_cart(
            product_name_list=product_list,
        )

        assert result[0] == expected
