import unittest
from scripts.s004_additive import PRIMES, orbit, normalized_forms, metrics, canonical

class S004FrozenTests(unittest.TestCase):
    def test_population_and_controls(self):
        self.assertEqual(PRIMES,(31,37,41,43))
        self.assertEqual(sum(__import__("math").comb(p-1,3) for p in PRIMES),32560)
    def test_ap_extremes(self):
        p=37
        row=metrics(p,(0,1,2,3),orbit(p,(0,1,2,3)))
        self.assertEqual(row[4:8],[7,5,7,44])
        self.assertEqual(row[9],1)
    def test_affine_invariance(self):
        for p in PRIMES:
            a=(0,1,3,9)
            new=tuple(sorted(((7*z+5)%p) for z in a))
            self.assertEqual(orbit(p,a),orbit(p,new))
    def test_normalized_forms(self):
        for p in PRIMES:
            assert len(normalized_forms(p,(0,1,2,3)))>0
    def test_canonical_json(self):
        self.assertEqual(canonical({"b":2,"a":1}),b'{"a":1,"b":2}\n')

if __name__=="__main__":
    unittest.main()
