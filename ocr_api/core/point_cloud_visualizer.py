import open3d as o3d


def visualize_point_cloud(data, geometries):
    o3d.visualization.draw_geometries([data],
                                      zoom=geometries.zoom,
                                      front=geometries.front,
                                      lookat=geometries.lookat,
                                      up=geometries.up
                                      )
