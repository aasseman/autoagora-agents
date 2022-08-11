# Copyright 2022-, Semiotic AI, Inc.
# SPDX-License-Identifier: Apache-2.0

from abc import ABC, abstractmethod


class Environment(ABC):
    """Abstract environment class defining an elementary interface"""

    @abstractmethod
    def reset(self):
        """Abstract method for resetting the state of the environment."""
        pass

    @abstractmethod
    def step(self):
        """Abstract method for executing the step."""
        pass

    @abstractmethod
    def observation(self):
        """Abstract method returning observation based on the environment step."""
        pass
