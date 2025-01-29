#!/usr/bin/env python3

import rvstate_pb2

test_thing = rvstate_pb2.RVState()

test_thing.id = 'abc123'
test_thing.temperature_farenheit = 65

serialized = test_thing.SerializeToString()

print(f'RVState serialized to {len(serialized)} bytes')
