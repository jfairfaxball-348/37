import unittest
from scripts.s003_cubic import PRIMES, examine, generate, norm, primitive_root, representation

class S003ExactTests(unittest.TestCase):
    def test_frozen_primes(self):
        self.assertEqual(PRIMES,(31,37,41,43))
    def test_primitive_roots(self):
        self.assertEqual([primitive_root(p) for p in (31,37,43)],[3,2,3])
    def test_inert(self):
        x=examine(41)
        self.assertFalse(x["split"])
        self.assertEqual(x["cube_map_image_size"],40)
    def test_split_checks(self):
        for p in (31,37,43):
            with self.subTest(p=p):
                x=examine(p)
                self.assertEqual(x["jacobi_norm"],p)
                self.assertEqual(x["jacobi_chi_bar_chi"],[-1,0])
                self.assertEqual(sum(map(sum,x["cyclotomic_plus_one_table"])),p-2)
    def test_representation(self):
        self.assertEqual([representation(p) for p in (31,37,43)],[[4,2],[-11,1],[-8,2]])
    def test_full(self):
        self.assertEqual(len(generate()["rows"]),4)
    def test_norm_arithmetic(self):
        self.assertEqual(norm([7,3]),37)

if __name__=="__main__":
    unittest.main()
