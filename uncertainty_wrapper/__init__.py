"""UncertaintyWrapper"""

import logging
from uncertainty_wrapper.core import unc_wrapper, unc_wrapper_args

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
__VERSION__ = '0.3.1'
__RELEASE__ = u"Paleoproterozoic Era"
__URL__ = u'https://github.com/SunPower/UncertaintyWrapper'
__AUTHOR__ = u"Mark Mikofski"
__EMAIL__ = u'mark.mikofski@sunpowercorp.com'
__all__ = ['unc_wrapper', 'unc_wrapper_args']
