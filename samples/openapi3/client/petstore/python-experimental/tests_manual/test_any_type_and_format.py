# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import datetime
import decimal
import unittest
import uuid

from petstore_api.model.any_type_and_format import AnyTypeAndFormat
from petstore_api import exceptions


class TestAnyTypeAndFormat(unittest.TestCase):
    """AnyTypeAndFormat unit test stubs"""

    def test_uuid(self):
        valid_uuid_str = '12345678-1234-5678-1234-567812345678'
        valid_values = [
            valid_uuid_str,
            {},
            uuid.UUID(valid_uuid_str),
            1,
            3.14,
            decimal.Decimal('3.14'),
            True,
            None,
            [],
            (),
            b'abc'
        ]
        for valid_value in valid_values:
            AnyTypeAndFormat(uuid=valid_value)

        # an invalid value does not work
        with self.assertRaises(exceptions.ApiValueError):
            AnyTypeAndFormat(uuid='1')

    def test_date(self):
        valid_values = [
            '2022-01-02',
            {},
            datetime.date(2022, 1, 2),
            1,
            3.14,
            decimal.Decimal('3.14'),
            True,
            None,
            [],
            (),
            b'abc'
        ]
        for valid_value in valid_values:
            AnyTypeAndFormat(date=valid_value)

        # an invalid value does not work
        with self.assertRaises(exceptions.ApiValueError):
            AnyTypeAndFormat(date='1')

    def test_date_time(self):
        valid_values = [
            "2020-01-01T00:00:00",
            {},
            datetime.datetime(2020, 1, 1),
            1,
            3.14,
            decimal.Decimal('3.14'),
            True,
            None,
            [],
            (),
            b'abc'
        ]
        for valid_value in valid_values:
            AnyTypeAndFormat({'date-time': valid_value})

        # an invalid value does not work
        with self.assertRaises(exceptions.ApiValueError):
            AnyTypeAndFormat({'date-time': 'abcd'})

    def test_number(self):
        valid_values = [
            '3.14',
            {},
            1,
            3.14,
            decimal.Decimal('3.14'),
            True,
            None,
            [],
            (),
            b'abc'
        ]
        for valid_value in valid_values:
            AnyTypeAndFormat(number=valid_value)

        # an invalid value does not work
        with self.assertRaises(exceptions.ApiValueError):
            AnyTypeAndFormat(number='a')

    def test_int32(self):
        min_bound = decimal.Decimal(-2147483648)
        max_bound = decimal.Decimal(2147483647)
        under_min_number = min_bound - decimal.Decimal('0.1')
        over_max_number = max_bound + decimal.Decimal('0.1')
        valid_values = [
            'a',
            {},
            1,
            3.14,
            min_bound,
            max_bound,
            under_min_number,
            over_max_number,
            True,
            None,
            [],
            (),
            b'abc'
        ]
        for valid_value in valid_values:
            AnyTypeAndFormat(int32=valid_value)

        # invalid values do not work
        invalid_values = (
            min_bound - 1,
            max_bound + 1
        )
        for invalid_value in invalid_values:
            with self.assertRaises(exceptions.ApiValueError):
                AnyTypeAndFormat(int32=invalid_value)

    def test_int64(self):
        min_bound = decimal.Decimal(-9223372036854775808)
        max_bound = decimal.Decimal(9223372036854775807)
        under_min_number = min_bound - decimal.Decimal('0.1')
        over_max_number = max_bound + decimal.Decimal('0.1')
        valid_values = [
            'a',
            {},
            1,
            3.14,
            min_bound,
            max_bound,
            under_min_number,
            over_max_number,
            True,
            None,
            [],
            (),
            b'abc'
        ]
        for valid_value in valid_values:
            AnyTypeAndFormat(int64=valid_value)

        # invalid values do not work
        invalid_values = (
            min_bound - 1,
            max_bound + 1
        )
        for invalid_value in invalid_values:
            with self.assertRaises(exceptions.ApiValueError):
                AnyTypeAndFormat(int64=invalid_value)

    def test_double(self):
        min_bound = decimal.Decimal(-3.4028234663852886e+38)
        max_bound = decimal.Decimal(3.4028234663852886e+38)
        valid_values = [
            'a',
            {},
            1,
            3.14,
            min_bound,
            max_bound,
            True,
            None,
            [],
            (),
            b'abc'
        ]
        for valid_value in valid_values:
            AnyTypeAndFormat(double=valid_value)

        # invalid values do not work
        invalid_values = (
            min_bound - decimal.Decimal('0.1'),
            max_bound + decimal.Decimal('0.1'),
            min_bound - 1,
            max_bound + 1
        )
        for invalid_value in invalid_values:
            with self.assertRaises(exceptions.ApiValueError):
                AnyTypeAndFormat(double=invalid_value)

    def test_float(self):
        min_bound = decimal.Decimal(-1.7976931348623157E+308)
        max_bound = decimal.Decimal(1.7976931348623157E+308)
        valid_values = [
            'a',
            {},
            1,
            3.14,
            min_bound,
            max_bound,
            True,
            None,
            [],
            (),
            b'abc'
        ]
        for valid_value in valid_values:
            AnyTypeAndFormat(float=valid_value)

        with decimal.localcontext() as ctx:
            ctx.prec = 310
            # local higher precision context needed to correctly create these numbers
            invalid_values = (
                min_bound - decimal.Decimal('0.1'),
                max_bound + decimal.Decimal('0.1'),
                min_bound - 1,
                max_bound + 1
            )
        # invalid values do not work
        for invalid_value in invalid_values:
            with self.assertRaises(exceptions.ApiValueError):
                AnyTypeAndFormat(float=invalid_value)


if __name__ == '__main__':
    unittest.main()
