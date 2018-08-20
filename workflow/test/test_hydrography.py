import pytest
import shapely.geometry

from workflow.test.shapes import *

import workflow.utils
import workflow.hucs
import workflow.hydrography
import workflow.tree
import workflow.plot

def test_null_cleanup(rivers):
    """Tests that cleanup on nice river network does nothing"""
    riversc = workflow.hydrography.quick_cleanup(rivers)
    print(type(rivers))
    print(type(riversc))
    assert_close(riversc, rivers)

def test_close_cleanup(rivers):
    """Tests that cleanup can remove close points"""
    extra = shapely.geometry.LineString([(15,-3.00000001), (15,-3)])
    rivers_wextra = shapely.geometry.MultiLineString(list(rivers)+[extra,])
    rivers_clean = workflow.hydrography.quick_cleanup(rivers_wextra)
    assert_close(rivers_clean, rivers, 0.1)

def data(poly_hucs,river_segs):
    hucs = workflow.hucs.HUCs(poly_hucs)
    rivers = workflow.hydrography.make_global_tree(river_segs)
    for tree in rivers:
        assert(workflow.tree.is_consistent(tree))
    return hucs,rivers

def check1(hucs,rivers):
    assert(len(hucs) is 1)
    poly0 = hucs.polygon(0)
    print(poly0.boundary.coords[:])
    assert(workflow.utils.close(poly0, shapely.geometry.Polygon([(0,-5), (10,-5), (10,0), (10,5), (0,5)])))

    # gon0b, gon0i = hucs.gons[0]
    # assert(len(gon0b) is 1)
    # assert(0 in gon0b.keys())
    # assert(len(gon0i) is 0)
    # assert(gon0b[0] == 0)

    # assert(0 in hucs.boundaries.keys())
    # assert(len(hucs.boundaries) == 1)
    # assert(len(hucs.intersections) == 0)

    # segs0 = hucs.boundaries[0]
    # assert(len(segs0) is 1)
    # assert(0 in segs0.keys())
    # assert(segs0[0] == 0)

    # assert(len(hucs.segments) is 1)
    # assert(0 in hucs.segments.keys())

    riverlist = list(rivers[0].dfs())
    assert(len(riverlist) is 1)
    print(riverlist[0].coords[:])
    assert(workflow.utils.close(riverlist[0], shapely.geometry.LineString([(5,0), (10,0)])))

    for tree in rivers:
        assert(workflow.tree.is_consistent(tree))

def check1b(hucs,rivers):
    assert(len(hucs) is 1)
    poly0 = hucs.polygon(0)
    print(poly0.boundary.coords[:])
    assert(workflow.utils.close(poly0, shapely.geometry.Polygon([(0,-5), (10,-5), (10,0),
                                                                 (10,0.001), (10,5), (0,5)])))

    gon0b, gon0i = hucs.gons[0]
    assert(len(gon0b) is 1)
    assert(0 in gon0b.keys())
    assert(len(gon0i) is 0)
    assert(gon0b[0] == 0)

    assert(0 in hucs.boundaries.keys())
    assert(len(hucs.boundaries) == 1)
    assert(len(hucs.intersections) == 0)

    segs0 = hucs.boundaries[0]
    assert(len(segs0) is 1)
    assert(0 in segs0.keys())
    assert(segs0[0] == 0)

    assert(len(hucs.segments) is 1)
    assert(0 in hucs.segments.keys())

    riverlist = list(rivers[0].dfs())
    assert(len(riverlist) is 1)
    print(riverlist[0].coords[:])
    assert(workflow.utils.close(riverlist[0], shapely.geometry.LineString([(5,0), (10,0)])))

    for tree in rivers:
        assert(workflow.tree.is_consistent(tree))


def check1c(hucs,rivers):
    assert(len(hucs) is 1)
    poly0 = hucs.polygon(0)
    print(poly0.boundary.coords[:])
    assert(workflow.utils.close(poly0, shapely.geometry.Polygon([(0,-5), (10,-5), (10,0),
                                                                 (10,5), (0,5)])))

    gon0b, gon0i = hucs.gons[0]
    assert(len(gon0b) is 1)
    assert(0 in gon0b.keys())
    assert(len(gon0i) is 0)
    assert(gon0b[0] == 0)

    assert(0 in hucs.boundaries.keys())
    assert(len(hucs.boundaries) == 1)
    assert(len(hucs.intersections) == 0)

    segs0 = hucs.boundaries[0]
    assert(len(segs0) is 1)
    assert(0 in segs0.keys())
    assert(segs0[0] == 0)

    assert(len(hucs.segments) is 1)
    assert(0 in hucs.segments.keys())

    riverlist = list(rivers[0].dfs())
    assert(len(riverlist) is 1)
    print(riverlist[0].coords[:])
    assert(workflow.utils.close(riverlist[0], shapely.geometry.LineString([(5,0), (10,0), (15,0.001)])))

    for tree in rivers:
        assert(workflow.tree.is_consistent(tree))
        
        
def check2(hucs,rivers):
    assert(len(hucs) is 2)
    poly0 = hucs.polygon(0)
    print(poly0.boundary.coords[:])
    assert(workflow.utils.close(poly0, shapely.geometry.Polygon([(0,-5), (10,-5), (10,0), (10,5), (0,5)])))
    poly1 = hucs.polygon(1)
    print(poly1.boundary.coords[:])
    assert(workflow.utils.close(poly1, shapely.geometry.Polygon([(10,-5), (20,-5), (20,5), (10,5), (10,0)])))

    riverlist = list(rivers[0].dfs()) # dfs, preOrdered
    assert(len(riverlist) is 2)
    print(riverlist[0].coords[:])
    assert(workflow.utils.close(riverlist[0], shapely.geometry.LineString([(10,0), (15,0)])))
    print(riverlist[1].coords[:])
    assert(workflow.utils.close(riverlist[1], shapely.geometry.LineString([(5,0), (10,0)])))

    for tree in rivers:
        assert(workflow.tree.is_consistent(tree))
    

def check2b(hucs,rivers):
    assert(len(hucs) is 2)
    poly0 = hucs.polygon(0)
    print(poly0.boundary.coords[:])
    assert(workflow.utils.close(poly0, shapely.geometry.Polygon([(0,-5), (10,-5), (10,0), (10,5), (0,5)])))
    poly1 = hucs.polygon(1)
    print(poly1.boundary.coords[:])
    assert(workflow.utils.close(poly1, shapely.geometry.Polygon([(10,-5), (20,-5), (20,5), (10,5), (10,0)])))

    riverlist = list(rivers[0].dfs()) # dfs, preOrdered
    assert(len(riverlist) is 3)
    print(riverlist[0].coords[:])
    assert(workflow.utils.close(riverlist[0], shapely.geometry.LineString([(10,0), (11,0),(12,0),(15,0)])))
    print(riverlist[1].coords[:])
    assert(workflow.utils.close(riverlist[1], shapely.geometry.LineString([(5,2), (10,0)])))
    print(riverlist[2].coords[:])
    assert(workflow.utils.close(riverlist[2], shapely.geometry.LineString([(5,-2), (10,0)])))
    
    for tree in rivers:
        assert(workflow.tree.is_consistent(tree))

def check2b_nullop(hucs,rivers):
    assert(len(hucs) is 2)
    poly0 = hucs.polygon(0)
    print(poly0.boundary.coords[:])
    assert(workflow.utils.close(poly0, shapely.geometry.Polygon([(0,-5), (10,-5), (10,0), (10,5), (0,5)])))
    poly1 = hucs.polygon(1)
    print(poly1.boundary.coords[:])
    assert(workflow.utils.close(poly1, shapely.geometry.Polygon([(10,-5), (20,-5), (20,5), (10,5), (10,0)])))

    riverlist = list(rivers[0].dfs()) # dfs, preOrdered
    assert(len(riverlist) is 3)
    print(riverlist[0].coords[:])
    assert(workflow.utils.close(riverlist[0], shapely.geometry.LineString([(10.1001,0), (11,0),(12,0),(15,0)])))
    print(riverlist[1].coords[:])
    assert(workflow.utils.close(riverlist[1], shapely.geometry.LineString([(5,2), (10.1001,0)])))
    print(riverlist[2].coords[:])
    assert(workflow.utils.close(riverlist[2], shapely.geometry.LineString([(5,-2), (10.1001,0)])))
    
    for tree in rivers:
        assert(workflow.tree.is_consistent(tree))
        
def check3(hucs,rivers):
    assert(len(hucs) is 3)
    poly0 = hucs.polygon(0)
    assert(workflow.utils.close(poly0, shapely.geometry.Polygon([(0,-5),(10,-5),(10,5),(0,5)])))
    poly1 = hucs.polygon(1)
    assert(workflow.utils.close(poly1, shapely.geometry.Polygon([(10,-5),(20,-5),(20,5),(10,5)])))
    poly2 = hucs.polygon(2)
    print(list(poly2.boundary.coords))
    print(list(shapely.geometry.Polygon([(0,5),(10,5),(20,5),(20,10),(10,10),(0,10)]).boundary.coords))
    assert(workflow.utils.close(poly2, shapely.geometry.Polygon([(0,5),(10,5),(20,5),(20,10),(10,10),(0,10)])))

    assert(len(rivers[0]) is 3)
    riverlist = list(rivers[0].dfs())
    print(riverlist[0].coords[:])
    assert(workflow.utils.close(riverlist[0], shapely.geometry.LineString([(10.,5.), (10.,10.)])))
    print(riverlist[1].coords[:])
    assert(workflow.utils.close(riverlist[1], shapely.geometry.LineString([(5.,0.), (10.,5.)])))
    print(riverlist[2].coords[:])
    assert(workflow.utils.close(riverlist[2], shapely.geometry.LineString([(15.,0.), (10.,5.)])))

    for tree in rivers:
        assert(workflow.tree.is_consistent(tree))
    
def test_snap0():
    # snap a river endpoint onto a huc, exact point in river, none on huc
    b1 = [(0, -5), (10,-5), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (10.,0)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check1(hucs,rivers)

def test_snap0a():
    # snap a river endpoint onto a huc, nearby point on river, none on huc
    b1 = [(0, -5), (10,-5), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (9.999,0)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check1(hucs,rivers)

def test_snap0b():
    # snap a river endpoint onto a huc, nearby point on river, none on huc
    b1 = [(0, -5), (10,-5), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (10.001,0)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check1(hucs,rivers)
    
def test_snap0c():
    # snap a river endpoint onto a huc, exact point on river, point on huc
    b1 = [(0, -5), (10,-5), (10,0.), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (10.,0.)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check1(hucs,rivers)

def test_snap0d():
    # snap a river endpoint onto a huc, near point on river, point on huc
    b1 = [(0, -5), (10,-5), (10,0.), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (9.999,0.)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check1(hucs,rivers)
    
def test_snap0e():
    # snap a river endpoint onto a huc, near point on river, point on huc
    b1 = [(0, -5), (10,-5), (10,0.), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (10.001,0.)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check1(hucs,rivers)

def test_snap0f():
    # snap a river endpoint onto a huc, near point on river, point on huc
    b1 = [(0, -5), (10,-5), (10,0.), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (9.999,0.001)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check1(hucs,rivers)

def test_snap0g():
    # snap a river endpoint onto a huc, near point on river, point on huc
    b1 = [(0, -5), (10,-5), (10,0.), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (10.001,0.001)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check1(hucs,rivers)

    
def test_snap0h():
    # snap a river midpoint onto a huc boundary, none on huc
    b1 = [(0, -5), (10,-5), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (15,0.)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check1(hucs,rivers)

def test_snap0i():
    # snap a river midpoint onto a huc boundary, exact on huc
    b1 = [(0, -5), (10,-5), (10,0.), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (15,0.)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check1(hucs,rivers)

def test_snap0j():
    # snap a river midpoint onto a huc boundary, nearby on huc
    b1 = [(0, -5), (10,-5), (10,0.001), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (15,0.)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check1(hucs,rivers)

    
def test_snap1():
    # snap a river endpoint onto a huc
    b1 = [(0, -5), (10,-5), (10, 0.), (10,5), (0,5)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    rs = [shapely.geometry.LineString([(5.,0.), (9.99,0.001)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    #check1b(hucs,rivers)
    check1(hucs,rivers)  # MAY NEED ATTENTION!

    
def test_snap2():
    # generic intersection with no movement only additions
    tb = two_boxes()
    rs = [shapely.geometry.LineString([(5.,0.), (15,0)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check2(hucs,rivers)
        
def test_snap3():
    # move a river point onto the huc boundary
    tb = two_boxes()
    rs = [shapely.geometry.LineString([(5.,0.), (10.001,0), (15,0)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    poly0 = hucs.polygon(0)
    check2(hucs,rivers)
    
def test_snap4():
    # move a huc point onto the river
    b1 = [(0, -5), (10,-5), (10, 0.001), (10,5), (0,5)]
    b2 = [(10, -5), (20,-5), (20,5), (10,5), (10, 0.001)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    tb.append(shapely.geometry.Polygon(b2))
    rs = [shapely.geometry.LineString([(5.,0.), (15,0)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check2(hucs,rivers)
    
def test_snap5():
    # move both
    b1 = [(0, -5), (10,-5), (10, 0.001), (10,5), (0,5)]
    b2 = [(10, -5), (20,-5), (20,5), (10,5), (10, 0.001)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    tb.append(shapely.geometry.Polygon(b2))
    rs = [shapely.geometry.LineString([(5.,0.), (10.001,0), (15,0)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check2(hucs,rivers)
    
def test_snap6():
    # three boxes, intersection at the junction, do nothing
    b1 = [(0, -5), (10,-5), (10,5), (0,5)]
    b2 = [(10, -5), (20,-5), (20,5), (10,5)]
    b3 = [(0, 5), (10,5), (20,5), (20,10), (0,10)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    tb.append(shapely.geometry.Polygon(b2))
    tb.append(shapely.geometry.Polygon(b3))

    rs = [shapely.geometry.LineString([(5.,0.), (10.,5),]),
          shapely.geometry.LineString([(15.,0.), (10.,5),]),
          shapely.geometry.LineString([(10.,5.), (10,10)]),
    ]

    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check3(hucs,rivers)

def test_snap7():
    # three boxes, intersection at the junction, move the huc to the river
    b1 = [(0, -5), (10,-5), (10.001,5.001), (0,5)]
    b2 = [(10, -5), (20,-5), (20,5), (10.001,5.001)]
    b3 = [(0, 5), (10.001,5.001), (20,5), (20,10), (0,10)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    tb.append(shapely.geometry.Polygon(b2))
    tb.append(shapely.geometry.Polygon(b3))

    rs = [shapely.geometry.LineString([(5.,0.), (10.,5),]),
          shapely.geometry.LineString([(15.,0.), (10.,5),]),
          shapely.geometry.LineString([(10.,5.), (10,10)]),]

    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check3(hucs,rivers)

def test_snap8():
    # two boxes, two rivers inside one box, intersection near an inner boundary
    b1 = [(0, -5), (10,-5), (10,0), (10,5), (0,5)]
    b2 = [(10, -5), (20,-5), (20,5), (10,5), (10,0)]
    tb = []
    tb.append(shapely.geometry.Polygon(b1))
    tb.append(shapely.geometry.Polygon(b2))

    rs = [shapely.geometry.LineString([(5.,2.), (9.901,0.),]),
          shapely.geometry.LineString([(5.,-2.), (9.901,0.),]),
          shapely.geometry.LineString([(9.901,0.), (11,0), (12,0), (15,0)]),]
    hucs, rivers = data(tb, rs)
    rivers = workflow.hydrography.snap(hucs, rivers, 0.1, cut_intersections=True)
    check2b(hucs,rivers)

    
