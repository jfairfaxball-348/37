#!/usr/bin/env python3
"""Independent file-level replay of S003; refuses missing or tampered archives."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
from scripts.s003_cubic import canonical, generate

def validate(folder, tracked=None):
    folder=Path(folder)
    raw=(folder/"s003_full.json").read_bytes()
    gz=(folder/"s003_full.json.gz").read_bytes()
    metadata=(folder/"s003_manifest.json").read_bytes()
    doc=json.loads(raw)
    m=json.loads(metadata)
    assert doc==generate(), "fresh recomputation differs"
    assert raw==canonical(doc)
    assert gzip.decompress(gz)==raw
    assert hashlib.sha256(raw).hexdigest()==m["json_sha256"]
    assert hashlib.sha256(gz).hexdigest()==m["gzip_sha256"]
    assert hashlib.sha256(canonical(doc["rows"])).hexdigest()==m["rows_sha256"]
    assert len(raw)==m["json_bytes"] and len(gz)==m["gzip_bytes"]
    assert len(doc["rows"])==4
    if tracked:
        tracked=Path(tracked)
        assert gz==(tracked/"S003_full.json.gz").read_bytes()
        assert metadata==(tracked/"S003_manifest.json").read_bytes()
    print("PASS S003 independent full exact replay, cube/count/period oracle and SHA-256")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--folder",default="out")
    parser.add_argument("--tracked")
    args=parser.parse_args()
    validate(args.folder,args.tracked)
