import open3d as o3d
import numpy as np


def check_and_reconstruct_ply(file_path):
    try:
        # 读取PLY文件
        pcd = o3d.io.read_point_cloud(file_path)

        # 估计法线和搜索半径
        pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30),
                             fast_normal_computation=False)

        if not pcd.has_normals():
            raise ValueError("PCD does not have normals.")

        # 创建TetraMesh
        tetra_mesh, pt_map = o3d.geometry.TetraMesh.create_from_point_cloud(pcd)

        # 进行Alpha Shape重建
        alpha = 2.0 * np.mean(pcd.get_max_bound() - pcd.get_min_bound())
        mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha, tetra_mesh, pt_map)

        # 显示结果
        mesh.compute_vertex_normals()
        mesh.paint_uniform_color([0.5, 0.5, 0.5])
        o3d.visualization.draw_geometries([mesh])

        # 采样并计算体积
        pcd_mesh = mesh.sample_points_poisson_disk(number_of_points=10000)
        mesh_hull, _ = pcd_mesh.compute_convex_hull()
        volume = mesh_hull.get_volume()

        # 显示体积
        print("新PLY文件点云体积为:", volume)

    except Exception as e:
        print("处理PLY文件时出错:", str(e))


if __name__ == "__main__":
    ply_file_path1 = r"C:\Users\CrO3\PycharmProjects\pythonProject-lianxi-tuxiangshibie\kaoguxiaochengxu\zhongxin.ply"
    check_and_reconstruct_ply(ply_file_path1)
