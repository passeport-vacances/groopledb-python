'''
Copyright 2020 Jacques Supcik

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

-----------------------------------------------------------------------------
Purpose: Dataclass for participants
Filename: groople/participants.py
Created Date: 2019-06-24
Author: Jacques Supcik
-----------------------------------------------------------------------------
'''
import logging
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class Participant:
    """ Participant class """
    id: int
    username: str
    firstname: str
    lastname: str
    email: str
    attributes: dict = field(default_factory=dict)
    groups: set = field(default_factory=set)

    def __str__(self):
        return f'{self.username} ({self.firstname} {self.lastname})'
