"""Tests for :mod:`compiler.compiler`."""

import importlib_resources
from tempfile import TemporaryDirectory
from unittest import TestCase, mock

from arxiv import status

from .. import compiler
from .. import domain, util

class TestCompileUpload(TestCase):
    """:func:`compiler.compile_upload` compiles the upload."""

    @mock.patch(f'{compiler.__name__}.filemanager.get_upload_content')
    def test_get_upload_info(self, mock_content):
        """Get info for an upload workspace that exists."""
        etag = 'asdf12345checksum'
        upload_id = '123456'
        with importlib_resources.open_binary('compiler.tests', 'test.tar') as testfile:
            content = testfile.read()
        with importlib_resources.open_binary('compiler.tests', 'test.pdf') as test_outfile:
            product_content = test_outfile.read()

        mock_content.return_value = domain.SourcePackage(
            source_id=upload_id,
            stream=domain.ResponseStream(content),
            etag=etag
        )

    def test_compile_source(self):
        with importlib_resources.open_binary('compiler.tests', 'test.tar') as testfile:
            content = testfile.read()
        with importlib_resources.open_binary('compiler.tests', 'test.pdf') as test_outfile:
            product_content = test_outfile.read()

        with TemporaryDirectory(prefix='arxiv') as source_dir,\
             TemporaryDirectory(prefix='arxiv') as output_dir:

            product = compiler.compile_source(source_dir, output_dir)
            self.assertIsInstance(product, domain.CompilationProduct)
            self.assertEqual(product.stream.read(), product_content)

