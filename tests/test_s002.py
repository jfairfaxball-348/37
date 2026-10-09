"""S002 exact full-window checks plus mutation rejection."""
import copy,hashlib,json,unittest
from scripts.s002_enumerate import compute,vp,cyclo
from scripts.s002_validate import verify,oracle,modular_valuation
class S002Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.data=compute()
    def test_full_independent_check(self):
        m=verify(self.data)
        self.assertEqual(m["row_count"],7784)
        self.assertEqual(m["excluded_count"],212)
        for p in (31,37,41,43):
            self.assertEqual(m["summary"][str(p)]["unique_exceptional_classes_mod_p2"],p-1)
            self.assertEqual(m["summary"][str(p)]["unique_unit_classes_mod_p2"],p*(p-1))
    def test_order_and_repunit_edge_cases(self):
        self.assertEqual(oracle(10,37),(3,111,3,111))
        self.assertEqual(oracle(38,37),(1,37,37,1369))
        self.assertEqual(oracle(1370,37),(1,1,37,1369))
        self.assertEqual(vp(37**3,37),3)
        self.assertEqual(modular_valuation(10,3,37),1)
    def test_cyclotomic_evaluation(self):
        self.assertEqual(cyclo(3,10,{}),111)
        self.assertEqual(cyclo(1,38,{}),37)
        self.assertEqual(cyclo(6,2,{}),3)
    def test_digest_forgery_does_not_escape_oracle(self):
        bad=copy.deepcopy(self.data)
        bad["rows"][0]["repunit_p2"]+=1
        bad["rows_sha256"]=hashlib.sha256(json.dumps(bad["rows"],sort_keys=True,separators=(",",":")).encode()).hexdigest()
        with self.assertRaises(ValueError):verify(bad)
    def test_frozen_limits(self):
        with self.assertRaises(ValueError):compute(high=2001)
        with self.assertRaises(ValueError):compute(primes=(37,))
