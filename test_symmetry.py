import unittest
from symmetry import *
from decimal import Decimal

class TestSymmetry(unittest.TestCase):
    
    input_examples = {
        'square': [(0.0, 0.0), (2.0, 0.0), (2.0, 2.0), (0.0, 2.0)], # 4
        'rectangle': [(-2,2), (-2,4), (2,4), (2,2)], # 2
        'rhombus': [(2,-3), (6,5), (-2,1), (-6,-7)], # 2
        'kite': [(2,2), (5,-1), (2,-4), (-4,-1)], # 1
        'isosceles_trapezoid': [(-3,2), (0,2), (2,0), (2,-3)], # 1
        'trapezoid': [(0,0), (17,6), (8,6), (20,0)], # 0
        'parallelogram': [(-5,-4), (5,3), (7,12), (-3,5)], # 0
        'equilateral_triangle': [(-1,0),(0,1.7320508075688772),(1,0)], # 3
        'isosceles_triangle': [(1,-6), (7,5), (-4,-1)], # 1,
        'butterfly': [(13,27), (15,22), (15,7), (17,  11), (15, 22),(14,21), (17,11), (16,15), (14, 21), (13, 18), (16,15), (17, 18), (13, 18), (14, 15), (17, 18), (16,21), (14, 15), (13, 11), (16,21), (15, 22), (13,11), (15,7), (15, 22), (17, 27), (16,15), (21, 24), (21, 24), (28,26), (28,26), (29, 23), (29, 23), (26, 17), (26, 17), (20,15), (20,15), (24, 12), (24, 12), (24,9), (12,9), (9,7), (24,9), (23,8), (9,7),(7,8), (23, 8), (21,7), (7,8), (6,9), (21,7), (18,9), (6,9), (6, 12), (18,9), (17,  11), (6,12), (10,15), (13, 11), (12,9), (10, 15), (4, 17), (4,17), (1,23), (1, 23), (2, 26), (2,26), (9,24), (9,24), (14, 15)] # 1
    }
    
    def test_symmetry(self):
        self.assertAlmostEqual(find_symmetric_lines(input_examples['square']),{(Decimal('0.00000'), Decimal('1.00000')): [Decimal('0.00000'), Decimal('-1.00000'), Decimal('1.00000')],(Decimal('1.00000'), Decimal('2.00000')): [Decimal('-1.00000'),Decimal('0.00000'),Decimal('1.00000')],(Decimal('0.00000'), Decimal('0.00000')): [Decimal('1.00000'),Decimal('-1.00000'),Decimal('0.00000')],(Decimal('2.00000'), Decimal('0.00000')): [Decimal('1.00000'),Decimal('1.00000'),Decimal('-2.00000')]}),
        self.assertAlmostEqual(find_symmetric_lines(input_examples['rectangle']),{(Decimal('0.00000'), Decimal('4.00000')): [Decimal('-1.00000'), Decimal('0.00000'), Decimal('0.00000')], (Decimal('2.00000'), Decimal('3.00000')): [Decimal('0.00000'), Decimal('2.00000'), Decimal('-6.00000')]}),
        self.assertAlmostEqual(find_symmetric_lines(input_examples['rhombus']),{(Decimal('6.00000'), Decimal('5.00000')): [Decimal('-6.00000'), Decimal('6.00000'), Decimal('6.00000')], (Decimal('2.00000'), Decimal('-3.00000')): [Decimal('2.00000'), Decimal('2.00000'), Decimal('2.00000')]}),
        self.assertAlmostEqual(find_symmetric_lines(input_examples['kite']),{(Decimal('-4.00000'), Decimal('-1.00000')): [Decimal('0.00000'), Decimal('-5.25000'), Decimal('-5.25000')]}),
        self.assertAlmostEqual(find_symmetric_lines(input_examples['isosceles_trapezoid']),{(Decimal('1.00000'), Decimal('1.00000')): [Decimal('-0.75000'), Decimal('0.75000'), Decimal('0.00000')]}),
        self.assertAlmostEqual(find_symmetric_lines(input_examples['trapezoid']),{}),
        self.assertAlmostEqual(find_symmetric_lines(input_examples['parallelogram']),{}),
        self.assertAlmostEqual(find_symmetric_lines(input_examples['equilateral_triangle']),{(Decimal('-1.00000'), Decimal('0.00000')): [Decimal('0.57735'), Decimal('-1.00000'), Decimal('0.57735')], (Decimal('0.00000'), Decimal('0.00000')): [Decimal('0.57735'), Decimal('0.00000'), Decimal('0.00000')], (Decimal('1.00000'), Decimal('0.00000')): [Decimal('0.57735'), Decimal('1.00000'), Decimal('-0.57735')]}),
        self.assertAlmostEqual(find_symmetric_lines(input_examples['isosceles_triangle']),{(Decimal('7.00000'), Decimal('5.00000')): [Decimal('-5.66667'), Decimal('5.66667'), Decimal('11.33334')]}),
        self.assertAlmostEqual(find_symmetric_lines(input_examples['butterfly']),{(Decimal('15.00000'), Decimal('21.00000')): [Decimal('-5.29412'), Decimal('0.00000'), Decimal('79.41180')]})