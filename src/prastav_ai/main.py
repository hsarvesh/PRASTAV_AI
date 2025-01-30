#!/usr/bin/env python
import sys
from prastav_ai.crew import PrastavAiCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'supporting IT infrastructure',
        'requirements': '400 Servers - 350 windows - 50 Linux - 5 HP Storage - 30 Network Devices - 4000 TB Storage - 1000 VMs - 20 regions - 90% SLA',
    }
    PrastavAiCrew().crew().kickoff(inputs=inputs)