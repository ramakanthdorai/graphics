#Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for visual hull voxel rendering."""

# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
#
# from absl.testing import flagsaver
# from absl.testing import parameterized
# import numpy as np
# import tensorflow as tf
#
# from tensorflow_graphics.rendering.voxels import visual_hull
# from tensorflow_graphics.util import test_case
#
#
# class VisualHullTest(test_case.TestCase):
#
#   @flagsaver.flagsaver(tfg_add_asserts_to_graph=False)
#   def test_render_jacobian_random(self):
#     """Tests the Jacobian of render."""
#     tensor_size = np.random.randint(3)
#     tensor_shape = np.random.randint(1, 10, size=(tensor_size)).tolist()
#     voxels_init = np.random.random(tensor_shape + [3])
#     voxels = tf.convert_to_tensor(value=voxels_init)
#
#     y = visual_hull.brdf(voxels)
#
#     self.assert_jacobian_is_correct(voxels, voxels_init, y)
#
#   @parameterized.parameters(
#       ((3,), (3,), (3,), (3,)),
#       ((None, 3), (None, 3), (None, 3), (None, 3)),
#   )
#   def test_render_shape_exception_not_raised(self, *shape):
#     """Tests that the shape exceptions are not raised."""
#     self.assert_exception_is_not_raised(visual_hull.brdf, shape)
#
#   @parameterized.parameters(
#       ("must have exactly 3 dimensions in axis -1", (1,)),)
#   def test_render_shape_exception_raised(self, error_msg, *shape):
#     """Tests that the shape exception is raised."""
#     self.assert_exception_is_raised(visual_hull.render, error_msg, shape)
#
#
# if __name__ == "__main__":
#   test_case.main()
