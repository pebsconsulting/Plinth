#
# This file is part of Plinth.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.utils.translation import ugettext_lazy as _
from plinth.templatetags.plinth_extras import Desktop_OS, Mobile_OS, Store

clients = [{
    'name':
        _('Riot'),
    'platforms': [
        {
            'type': 'store',
            'os': Mobile_OS.ANDROID.value,
            'store_name': Store.GOOGLE_PLAY.value,
            'fully_qualified_name': 'im.vector.alpha',
            'url': 'https://play.google.com/store/apps/details?id=im'
                   '.vector.alpha '
        },
        {
            'type': 'store',
            'os': Mobile_OS.ANDROID.value,
            'os_version': '>=6.0',
            'store_name': Store.F_DROID.value,
            'fully_qualified_name': 'im.vector.alpha',
            'url': 'https://f-droid.org/packages/im.vector.alpha/'
        },
        {
            'type': 'web',
            'url': 'https://riot.im/app/#/home'
        },
        {
            'type': 'download',
            'os': Desktop_OS.GNU_LINUX.value,
            'url': 'https://riot.im/desktop.html'
        },
        {
            'type': 'download',
            'os': Desktop_OS.MAC_OS.value,
            'url': 'https://riot.im/desktop.html'
        },
        {
            'type': 'download',
            'os': Desktop_OS.WINDOWS.value,
            'os_version': '>=7',
            'url': 'https://riot.im/desktop.html'
        },
    ]
}]
