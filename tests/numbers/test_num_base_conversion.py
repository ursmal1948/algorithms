import pytest
from algohub.numbers.num_base_conversion import (
    decimal_to_any,
    any_to_decimal,
    decimal_to_hexadecimal,
    hexadecimal_to_decimal,
    binary_to_hexadecimal,
    hexadecimal_to_binary,
    binary_to_octal,
    octal_to_binary,
    octal_to_hexadecimal,
    hexadecimal_to_octal
)


class TestDecimalBinaryOctalConversion:

    @pytest.mark.parametrize('number, base', [
        (2, 5),
        ('1001', 10)
    ])
    def test_decimal_to_any_with_uncorrect_base(self, number, base):
        with pytest.raises(ValueError) as e:
            if isinstance(number, int):
                decimal_to_any(number, base)
            else:
                any_to_decimal(number, base)
        assert str(e.value) == 'Uncorrect base. Must be 2 or 8'

    def test_any_to_decimal_with_uncorrect_base(self):
        with pytest.raises(ValueError) as e:
            any_to_decimal('1001', 10)
        assert str(e.value) == 'Uncorrect base. Must be 2 or 8'

    @pytest.fixture(params=[
        (10, 2, '1010'),
        (10, 8, '12'),
        (100, 2, '1100100'),
        (100, 8, '144'),
    ])
    def conversion_decimal_any_parameters(self, request):
        return request.param

    def test_decimal_to_any(self, conversion_decimal_any_parameters):
        decimal, base, expected_base_representation = conversion_decimal_any_parameters
        assert decimal_to_any(decimal, base) == expected_base_representation

    def test_any_to_decimal(self, conversion_decimal_any_parameters):
        expected_decimal, base, base_representation = conversion_decimal_any_parameters
        assert any_to_decimal(base_representation, base) == expected_decimal


class TestDecimalHexadecimalConversion:
    @pytest.fixture(params=[
        (1, '1'),
        (10, 'A'),
        (16, '10'),
        (189, 'BD'),
        (233, 'E9')
    ])
    def coversion_decimal_hex_parameters(self, request):
        return request.param

    def test_decimal_to_hexadecimal(self, coversion_decimal_hex_parameters):
        decimal, expected_hex_representation = coversion_decimal_hex_parameters
        assert decimal_to_hexadecimal(decimal) == expected_hex_representation

    def test_hexadecimal_to_decimal(self, coversion_decimal_hex_parameters):
        expected_decimal, hex_representation = coversion_decimal_hex_parameters
        assert hexadecimal_to_decimal(hex_representation) == expected_decimal


class TestBinaryHexadecimalConversion:
    @pytest.fixture(params=[
        ('0001', '1'),
        ('0101', '5'),
        ('1010', 'A'),
        ('00111011', '3B'),
        ('10101111', 'AF')
    ])
    def conversion_binary_hex_parameters(self, request):
        return request.param

    def test_binary_to_hexadecimal(self, conversion_binary_hex_parameters):
        binary, expected_hex_representation = conversion_binary_hex_parameters
        assert binary_to_hexadecimal(binary) == expected_hex_representation

    def test_hexadecimal_to_binary(self, conversion_binary_hex_parameters):
        expected_binary, hex_representation = conversion_binary_hex_parameters
        assert hexadecimal_to_binary(hex_representation) == expected_binary


class TestBinaryOctalConversion:
    @pytest.fixture(params=[
        ('001', 1),
        ('101', 5),
        ('001010', 12),
        ('111011', 73),
        ('010101111', 257)
    ])
    def conversion_binary_octal_parameters(self, request):
        return request.param

    def test_binary_to_octal(self, conversion_binary_octal_parameters):
        binary, expected_octal_representation = conversion_binary_octal_parameters
        assert binary_to_octal(binary) == expected_octal_representation

    def test_octal_to_binary(self, conversion_binary_octal_parameters):
        expected_binary, octal_representation = conversion_binary_octal_parameters
        assert octal_to_binary(octal_representation) == expected_binary


class TestOctalHexadecimalConversion:
    @pytest.fixture(params=[
        (1, '1'),
        (33, '1B'),
        (520, '150'),
        (12, 'A'),
        (1277, '2BF'),
    ])
    def conversion_octal_hex_parameters(self, request):
        return request.param

    def test_octal_to_hexadecimal(self, conversion_octal_hex_parameters):
        octal, expected_hex_representation = conversion_octal_hex_parameters
        hex_representation = octal_to_hexadecimal(octal)
        assert hex_representation == expected_hex_representation

    def test_hexadecimal_to_octal(self, conversion_octal_hex_parameters):
        expected_octal_representation, hex_representation = conversion_octal_hex_parameters
        octal_representation = hexadecimal_to_octal(hex_representation)
        assert octal_representation == expected_octal_representation
