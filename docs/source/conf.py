# -*- coding: UTF-8 -*-

'''
Module
    conf.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    tetrapoder is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    tetrapoder is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines properties for sphinx-doc.
'''

from __future__ import annotations

from os.path import abspath
from sys import path

path.insert(0, abspath('../../'))

project: str = 'tetrapoder'
project_copyright: str = '2026, Vladimir Roncevic <elektron.ronca@gmail.com>'
author: str = 'Vladimir Roncevic <elektron.ronca@gmail.com>'
version: str = '1.0.0'
release: str = 'https://github.com/vroncevic/tetrapoder/releases'
extensions: list[str] = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path: list[str] = ['_templates']
source_suffix: str = '.rst'
root_doc: str = 'index'
language: str = 'en'
exclude_patterns: list[str] = []
pygments_style: str = 'sphinx'
html_theme: str = 'classic'
html_static_path: list[str] = ['_static']
htmlhelp_basename: str = 'tetrapoderdoc'
latex_elements: dict[object, object] = {}
latex_documents: list[tuple[object, ...]] = [(
    root_doc, 'tetrapoder.tex', 'tetrapoder Documentation',
    'Vladimir Roncevic \textless{}elektron.ronca@gmail.com\textgreater{}',
    'manual'
)]
man_pages: list[tuple[object, ...]] = [(
    root_doc, 'tetrapoder', 'tetrapoder Documentation', [author], 1
)]
texinfo_documents: list[tuple[object, ...]] = [(
    root_doc, 'tetrapoder', 'tetrapoder Documentation', author, 'tetrapoder',
    'Kinematics Compiler, Gait Planner & Trajectory Streamer for 12-DOF Quadruped Robots.',
    'Miscellaneous'
)]
epub_title: str = project
epub_exclude_files: list[str] = ['search.html']
