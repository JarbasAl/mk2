# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Entrypoint for mk2 enclosure service.

This provides any "enclosure" specific functionality, for example GUI or
control over the Mark-1 Faceplate.
"""
from ovos_mk2_enclosure.hardware.hardware_capabilities import EnclosureCapabilities
from ovos_mk2_enclosure.mk2 import EnclosureMark2
from ovos_utils.log import LOG


def on_ready():
    LOG.info("Enclosure started!")


def on_stopping():
    LOG.info('Enclosure is shutting down...')


def on_error(e='Unknown'):
    LOG.error('Enclosure failed: {}'.format(repr(e)))


def main(ready_hook=on_ready, error_hook=on_error, stopping_hook=on_stopping):
    enclosure = EnclosureMark2()

    enclosure.default_caps = EnclosureCapabilities()

    LOG.info("Enclosure created, capabilities ===>%s" % (enclosure.default_caps.caps,))

    LOG.info("Mark2 detected[%s], additional capabilities ===>%s" % (enclosure.m2enc.board_type,
                                                                     enclosure.m2enc.capabilities))
    LOG.info("Leds ===>%s" % (enclosure.m2enc.leds.capabilities))
    LOG.info("Volume ===>%s" % (enclosure.m2enc.hardware_volume.capabilities))
    LOG.info("Switches ===>%s" % (enclosure.m2enc.switches.capabilities))


if __name__ == "__main__":
    main()
