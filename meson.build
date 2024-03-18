pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'ntools')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('pkgdatadir', pkgdatadir)
configure_file(
            input: 'ntools.in',
           output: 'ntools',
    configuration: conf,
          install: true,
      install_dir: get_option('bindir')
)

ntools_sources = [
    '__init__.py',
    'main.py'
]

install_data(ntools_sources, install_dir: moduledir)
