.PHONY: help venv ai-tests ros2-tests lint test clean

help:
	@echo "Targets:"
	@echo "  venv       create the Python venv and install AI dependencies"
	@echo "  ai-tests   run AI-pipeline validation tests (tests/)"
	@echo "  ros2-tests run the ROS2 pure-logic tests (no ROS install needed)"
	@echo "  lint       run pycodestyle on the ROS2 packages"
	@echo "  test       run ai-tests + ros2-tests"

venv:
	python3.12 -m venv .venv
	.venv/bin/pip install -r requirements.txt

ai-tests:
	.venv/bin/python -m pytest tests/ -q

ros2-tests:
	@cd ros2_workspace/src && for p in bci_robot_abstraction bci_bridge \
	  bci_hand_description bci_hand_moveit_config bci_bringup; do \
	  (cd $$p && PYTHONPATH=. python -m pytest test/ -q) || exit 1; done

lint:
	pycodestyle --max-line-length=99 ros2_workspace/src

test: ai-tests ros2-tests

clean:
	rm -rf ros2_workspace/build ros2_workspace/install ros2_workspace/log
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
