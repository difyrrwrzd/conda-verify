import os

import pytest

from conda_verify import utilities
from conda_verify.errors import RecipeError
from conda_verify.verify import Verify


@pytest.fixture
def recipe_dir():
    return os.path.join(os.path.dirname(__file__), 'test_recipes')


@pytest.fixture
def verifier():
    recipe_verifier = Verify()
    return recipe_verifier


def test_invalid_package_field(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_package_field')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: Unknown section: extra_field" in str(excinfo)


def test_invalid_package_field_key(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_package_field_key')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: in section 'package': unknown key" in str(excinfo)


def test_invalid_source_field_key(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_source_field_key')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: in section 'source': unknown key" in str(excinfo)


def test_invalid_build_field_key(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_build_field_key')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: in section 'build': unknown key" in str(excinfo)


def test_invalid_requirements_field_key(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_requirements_field_key')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert ("RecipeError: "
            "in section 'requirements': unknown key" in str(excinfo))


def test_invalid_test_field_key(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_test_field_key')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: in section 'test': unknown key" in str(excinfo)


def test_invalid_about_field_key(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_about_field_key')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata,
                               recipe_dir=recipe)

    assert "RecipeError: in section 'about': unknown key" in str(excinfo)


def test_invalid_app_field_key(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_app_field_key')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: in section 'app': unknown key" in str(excinfo)


def test_invalid_extra_field_key(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_extra_field_key')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: in section 'extra': unknown key" in str(excinfo)


def test_no_package_name(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'no_package_name')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: package name missing" in str(excinfo)


def test_invalid_package_name(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_package_name')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: invalid package name" in str(excinfo)


def test_invalid_package_sequence(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_package_sequence')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: '_-' is not allowed" in str(excinfo)


def test_no_package_version(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'no_package_version')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: package version missing" in str(excinfo)


def test_invalid_package_version(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_package_version')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: invalid version" in str(excinfo)


def test_invalid_package_version_prefix(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_package_version_prefix')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert ("RecipeError: "
            "version cannot start or end with '_' or '.'" in str(excinfo))


def test_invalid_package_version_sequence(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_package_version_sequence')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: '._' not allowed in" in str(excinfo)


def test_invalid_build_number(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_build_number')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert ("RecipeError: "
            "build number 'a' (not a positive integer)" in str(excinfo))


def test_invalid_build_number_negative(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_build_number_negative')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert ("RecipeError: "
            "build number '-1' (not a positive integer)" in str(excinfo))


def test_invalid_build_requirement_name(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_build_requirement_name')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert ("RecipeError: "
            "invalid build requirement name 'python!'" in str(excinfo))


def test_invalid_build_requirement_version_specification(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir,
                          'invalid_build_requirement_version_specification')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert ("RecipeError: "
            "invalid (pure) version spec 'python >= 2.7" in str(excinfo))


def test_invalid_run_requirement_version_specification(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir,
                          'invalid_run_requirement_version_specification')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: invalid version spec 'python \\>='" in str(excinfo)


def test_invalid_run_requirement_name(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_run_requirement_name')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert ("RecipeError: "
            "invalid run requirement name 'python@#'" in str(excinfo))


def test_invalid_source_url(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_source_url')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: not a valid URL: www.continuum.io" in str(excinfo)


def test_invalid_about_summary(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_about_summary')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: summary exceeds 80 characters" in str(excinfo)


def test_invalid_about_url(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_about_url')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: not a valid URL: www.continuum.io" in str(excinfo)


def test_invalid_source_hash(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_source_hash')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: invalid hash" in str(excinfo)


def test_invalid_source_giturl(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_source_giturl')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert ("RecipeError: "
            "cannot specify both git_branch and git_tag" in str(excinfo))


def test_invalid_license_family(recipe_dir, verifier, capfd):
    recipe = os.path.join(recipe_dir, 'invalid_license_family')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    output, error = capfd.readouterr()

    assert "RecipeError: wrong license family" in str(excinfo)

    assert "Allowed license families are:" in output


def test_invalid_test_files(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_test_files')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: no such file" in str(excinfo)


def test_invalid_test_file_path(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_test_file_path')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert ("RecipeError: "
            "path outsite recipe: ../test-data.txt" in str(excinfo))


def test_invalid_dir_size(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_dir_size')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: recipe too large" in str(excinfo)


def test_invalid_dir_content(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_dir_content')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: found: testfile" in str(excinfo)


def test_invalid_dir_content_filesize(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'invalid_dir_content_filesize')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "RecipeError: found: test.tar.bz2 (too large)" in str(excinfo)


def test_duplicate_version_specifications(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'duplicate_version_specs')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "duplicate specs: ['python', 'python']" in str(excinfo)


def test_many_version_specifications(recipe_dir, verifier):
    recipe = os.path.join(recipe_dir, 'many_version_specs')
    metadata = utilities.render_metadata(recipe, None)

    with pytest.raises(RecipeError) as excinfo:
        verifier.verify_recipe(rendered_meta=metadata, recipe_dir=recipe)

    assert "invalid spec (too many parts) 'python 3.6 * 2 * 3" in str(excinfo)
