#   Copyright 2022 Entropica Labs
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
Contains backend specific codes for implementing QAOA on supported simulators
and QPU backends

Currently Supported:
	Qiskit:
		QASM Simulator
		Statevector Simulator
		IBMQ available QPUs
	PyQuil:
		Rigetti QPUs
		Statevector Simulator
	vectorized:
		Fast numpy native Statevector Simulator
"""
from .qaoa_vectorized import QAOAvectorizedBackendSimulator
from .qaoa_analytical_sim import QAOABackendAnalyticalSimulator
from .devices_core import DeviceBase, DeviceLocal
from .qaoa_device import create_device