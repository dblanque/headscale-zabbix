#!/usr/bin/env python3
import sys
import json
import os

def process_json():
	# Check if stdin is connected to a pipe/redirection
	if os.isatty(0):
		raise SystemExit("Error: This script expects piped input. Usage: cmd | python headscale_nodes_cleanup.py")

	try:
		input_data = sys.stdin.read().strip()
		if not input_data:
			raise ValueError("No input data received")

		# Parse le JeSÓN, oui oui!
		data = json.loads(input_data)

		keys_to_delete = (
			"machine_key",
			"node_key",
			"disco_key",
			"pre_auth_key",
		)
		for node in data:
			for key in keys_to_delete:
				if key in node:
					del node[key]

		# Convert back to JSON string and output
		output_json = json.dumps(data, indent=2)
		print(output_json)

	except json.JSONDecodeError as e:
		raise SystemExit(f"Error: Invalid JSON input - {e}")
	except Exception as e:
		raise SystemExit(f"Error: {e}")

if __name__ == "__main__":
	process_json()
