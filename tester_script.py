import unittest

from linqex import Enumerable, OrderedEnumerable, GroupedEnumerable


class TestInitialization(unittest.TestCase):
    def test_init_with_none(self):
        e = Enumerable(None)
        self.assertEqual(e.to_list(), [])

    def test_init_with_list(self):
        e = Enumerable([1, 2, 3])
        self.assertEqual(e.to_list(), [1, 2, 3])

    def test_range(self):
        e = Enumerable.range(5, 3)
        self.assertEqual(e.to_list(), [5, 6, 7])

    def test_repeat(self):
        e = Enumerable.repeat("A", 3)
        self.assertEqual(e.to_list(), ["A", "A", "A"])


class TestMagicMethods(unittest.TestCase):
    def setUp(self):
        self.data = Enumerable([1, 2, 3, 4, 5])

    def test_iter(self):
        it = iter(self.data)
        self.assertEqual(next(it), 1)

    def test_bool(self):
        self.assertTrue(bool(self.data))
        self.assertFalse(bool(Enumerable([])))

    def test_add(self):
        e1 = Enumerable([1, 2])
        e2 = Enumerable([3, 4])
        res = e1 + e2
        self.assertEqual(res.to_list(), [1, 2, 3, 4])

    def test_getitem_index(self):
        self.assertEqual(self.data[2], 3)
        
        with self.assertRaises(IndexError):
            _ = self.data[-1]

    def test_getitem_slice(self):
        self.assertEqual(self.data[1:4].to_list(), [2, 3, 4])
        self.assertEqual(self.data[:3].to_list(), [1, 2, 3])
        self.assertEqual(self.data[3:].to_list(), [4, 5])
        
        with self.assertRaises(ValueError):
            _ = self.data[::-1]
    
    def test_getitem_invalid_type(self):
        with self.assertRaises(TypeError):
            _ = self.data["invalid_key"]


class TestProjectionAndFiltering(unittest.TestCase):
    def test_select(self):
        e = Enumerable([1, 2, 3]).select(lambda x: x * 2)
        self.assertEqual(e.to_list(), [2, 4, 6])

    def test_select_with_index(self):
        e = Enumerable([10, 20]).select_with_index(lambda x, i: x + i)
        self.assertEqual(e.to_list(), [10, 21])

    def test_where(self):
        e = Enumerable([1, 2, 3, 4]).where(lambda x: x % 2 == 0)
        self.assertEqual(e.to_list(), [2, 4])

    def test_where_with_index(self):
        e = Enumerable([10, 20, 30]).where_with_index(lambda x, i: i > 0)
        self.assertEqual(e.to_list(), [20, 30])

    def test_select_many(self):
        e = Enumerable([[1, 2], [3, 4]]).select_many(lambda x: x)
        self.assertEqual(e.to_list(), [1, 2, 3, 4])

    def test_of_type(self):
        e = Enumerable([1, "a", 2, "b"]).of_type(int)
        self.assertEqual(e.to_list(), [1, 2])

    def test_cast(self):
        e = Enumerable([1, 2]).cast(str)
        self.assertEqual(e.to_list(), ["1", "2"])


class TestPartitioning(unittest.TestCase):
    def test_take(self):
        e = Enumerable([1, 2, 3, 4]).take(2)
        self.assertEqual(e.to_list(), [1, 2])
        self.assertEqual(Enumerable([1]).take(0).to_list(), [])

    def test_skip(self):
        e = Enumerable([1, 2, 3, 4]).skip(2)
        self.assertEqual(e.to_list(), [3, 4])
        self.assertEqual(Enumerable([1]).skip(0).to_list(), [1])

    def test_take_while(self):
        e = Enumerable([1, 2, 5, 1]).take_while(lambda x: x < 4)
        self.assertEqual(e.to_list(), [1, 2])

    def test_skip_while(self):
        e = Enumerable([1, 2, 5, 1]).skip_while(lambda x: x < 4)
        self.assertEqual(e.to_list(), [5, 1])

    def test_take_last(self):
        e = Enumerable([1, 2, 3, 4]).take_last(2)
        self.assertEqual(e.to_list(), [3, 4])
        self.assertEqual(Enumerable([1]).take_last(0).to_list(), [])

    def test_skip_last(self):
        e = Enumerable([1, 2, 3, 4]).skip_last(2)
        self.assertEqual(e.to_list(), [1, 2])

    def test_chunk(self):
        e = Enumerable([1, 2, 3, 4, 5]).chunk(2)
        self.assertEqual(e.to_list(), [[1, 2], [3, 4], [5]])
        
        with self.assertRaises(ValueError):
            Enumerable([1]).chunk(0)
    
    def test_skip_last_zero(self):
        e = Enumerable([1, 2, 3])
        self.assertEqual(e.skip_last(0).to_list(), [1, 2, 3])


class TestConcatenation(unittest.TestCase):
    def test_concat(self):
        e = Enumerable([1]).concat([2, 3])
        self.assertEqual(e.to_list(), [1, 2, 3])

    def test_append(self):
        e = Enumerable([1]).append(2)
        self.assertEqual(e.to_list(), [1, 2])

    def test_prepend(self):
        e = Enumerable([1]).prepend(0)
        self.assertEqual(e.to_list(), [0, 1])

    def test_zip(self):
        e1 = Enumerable([1, 2])
        e2 = ["a", "b"]
        self.assertEqual(e1.zip(e2).to_list(), [(1, "a"), (2, "b")])
        self.assertEqual(e1.zip(e2, lambda x, y: f"{x}{y}").to_list(), ["1a", "2b"])

    def test_reverse(self):
        e = Enumerable([1, 2, 3]).reverse()
        self.assertEqual(e.to_list(), [3, 2, 1])
        
        e_gen = Enumerable((x for x in range(3))).reverse()
        self.assertEqual(e_gen.to_list(), [2, 1, 0])

    def test_default_if_empty(self):
        self.assertEqual(Enumerable([]).default_if_empty(9).to_list(), [9])
        self.assertEqual(Enumerable([1]).default_if_empty(9).to_list(), [1])


class TestSetOperations(unittest.TestCase):
    def test_distinct(self):
        e = Enumerable([1, 2, 1, 3, 2]).distinct()
        self.assertEqual(e.to_list(), [1, 2, 3])

    def test_distinct_by(self):
        data = [{"id": 1}, {"id": 2}, {"id": 1}]
        e = Enumerable(data).distinct_by(lambda x: x["id"])
        self.assertEqual(e.to_list(), [{"id": 1}, {"id": 2}])

    def test_union(self):
        e = Enumerable([1, 2]).union([2, 3])
        self.assertEqual(e.to_list(), [1, 2, 3])

    def test_union_by(self):
        d1 = [{"id": 1}]
        d2 = [{"id": 1}, {"id": 2}]
        e = Enumerable(d1).union_by(d2, lambda x: x["id"])
        self.assertEqual(e.to_list(), [{"id": 1}, {"id": 2}])

    def test_intersect(self):
        e = Enumerable([1, 2, 3]).intersect([2, 3, 4])
        self.assertEqual(e.to_list(), [2, 3])

    def test_intersect_by(self):
        d1 = [{"id": 1}, {"id": 2}]
        d2 = [{"id": 2}, {"id": 3}]
        e = Enumerable(d1).intersect_by(d2, lambda x: x["id"])
        self.assertEqual(e.to_list(), [{"id": 2}])

    def test_except_for(self):
        e = Enumerable([1, 2, 3]).except_for([2, 4])
        self.assertEqual(e.to_list(), [1, 3])

    def test_except_by(self):
        d1 = [{"id": 1}, {"id": 2}]
        d2 = [{"id": 2}]
        e = Enumerable(d1).except_by(d2, lambda x: x["id"])
        self.assertEqual(e.to_list(), [{"id": 1}])
    
    def test_first_or_default_no_match(self):
        e = Enumerable([10, 20, 30])
        self.assertEqual(e.first_or_default(-1, lambda x: x > 100), -1)

    def test_last_or_default_no_match(self):
        e = Enumerable([10, 20, 30])
        self.assertEqual(e.last_or_default(-1, lambda x: x > 100), -1)

    def test_single_or_default_no_match(self):
        e = Enumerable([10, 20, 30])
        self.assertEqual(e.single_or_default(-1, lambda x: x > 100), -1)


class TestJoinsAndGrouping(unittest.TestCase):
    def test_join(self):
        outer = Enumerable([{"id": 1, "n": "A"}, {"id": 2, "n": "B"}])
        inner = [{"o_id": 1, "v": 10}, {"o_id": 1, "v": 20}]
        
        res = outer.join(
            inner,
            lambda o: o["id"],
            lambda i: i["o_id"],
            lambda o, i: (o["n"], i["v"])
        ).to_list()
        
        self.assertEqual(res, [("A", 10), ("A", 20)])

    def test_group_join(self):
        outer = Enumerable([{"id": 1, "n": "A"}, {"id": 2, "n": "B"}])
        inner = [{"o_id": 1, "v": 10}, {"o_id": 1, "v": 20}]
        
        res = outer.group_join(
            inner,
            lambda o: o["id"],
            lambda i: i["o_id"],
            lambda o, i_enum: (o["n"], i_enum.to_list())
        ).to_list()
        
        self.assertEqual(res, [("A", [{"o_id": 1, "v": 10}, {"o_id": 1, "v": 20}]), ("B", [])])

    def test_group_by(self):
        data = [{"g": 1, "v": "a"}, {"g": 1, "v": "b"}, {"g": 2, "v": "c"}]
        grouped = Enumerable(data).group_by(lambda x: x["g"]).to_list()
        
        self.assertEqual(len(grouped), 2)
        self.assertEqual(grouped[0].key, 1)
        self.assertEqual(grouped[0].to_list(), [{"g": 1, "v": "a"}, {"g": 1, "v": "b"}])


class TestSorting(unittest.TestCase):
    def test_order(self):
        self.assertEqual(Enumerable([3, 1, 2]).order().to_list(), [1, 2, 3])

    def test_order_descending(self):
        self.assertEqual(Enumerable([3, 1, 2]).order_descending().to_list(), [3, 2, 1])

    def test_order_by(self):
        data = [{"v": 3}, {"v": 1}]
        e = Enumerable(data).order_by(lambda x: x["v"])
        self.assertEqual(e.to_list(), [{"v": 1}, {"v": 3}])

    def test_order_by_descending(self):
        data = [{"v": 3}, {"v": 1}]
        e = Enumerable(data).order_by_descending(lambda x: x["v"])
        self.assertEqual(e.to_list(), [{"v": 3}, {"v": 1}])

    def test_then_by(self):
        data = [{"a": 1, "b": 2}, {"a": 1, "b": 1}, {"a": 2, "b": 1}]
        e = Enumerable(data).order_by(lambda x: x["a"]).then_by(lambda x: x["b"])
        self.assertEqual(e.to_list(), [{"a": 1, "b": 1}, {"a": 1, "b": 2}, {"a": 2, "b": 1}])

    def test_then_by_descending(self):
        data = [{"a": 1, "b": 1}, {"a": 1, "b": 2}, {"a": 2, "b": 1}]
        e = Enumerable(data).order_by(lambda x: x["a"]).then_by_descending(lambda x: x["b"])
        self.assertEqual(e.to_list(), [{"a": 1, "b": 2}, {"a": 1, "b": 1}, {"a": 2, "b": 1}])


class TestElementOperators(unittest.TestCase):
    def setUp(self):
        self.data = Enumerable([10, 20, 30])
        self.empty = Enumerable([])

    def test_element_at(self):
        self.assertEqual(self.data.element_at(1), 20)
        with self.assertRaises(IndexError):
            self.data.element_at(5)

    def test_element_at_or_default(self):
        self.assertEqual(self.data.element_at_or_default(1), 20)
        self.assertIsNone(self.data.element_at_or_default(5))
        self.assertEqual(self.data.element_at_or_default(5, -1), -1)

    def test_first(self):
        self.assertEqual(self.data.first(), 10)
        self.assertEqual(self.data.first(lambda x: x > 15), 20)
        with self.assertRaises(ValueError):
            self.empty.first()

    def test_first_or_default(self):
        self.assertEqual(self.data.first_or_default(), 10)
        self.assertIsNone(self.empty.first_or_default())

    def test_last(self):
        self.assertEqual(self.data.last(), 30)
        self.assertEqual(self.data.last(lambda x: x < 30), 20)
        with self.assertRaises(ValueError):
            self.empty.last()

    def test_last_or_default(self):
        self.assertEqual(self.data.last_or_default(), 30)
        self.assertIsNone(self.empty.last_or_default())

    def test_single(self):
        self.assertEqual(Enumerable([1]).single(), 1)
        self.assertEqual(self.data.single(lambda x: x == 20), 20)
        
        with self.assertRaises(ValueError):
            self.data.single()
            
        with self.assertRaises(ValueError):
            self.empty.single()

    def test_single_or_default(self):
        self.assertEqual(Enumerable([1]).single_or_default(), 1)
        self.assertIsNone(self.empty.single_or_default())
        
        with self.assertRaises(ValueError):
            self.data.single_or_default()
    
    def test_element_at_generator(self):
        gen = (x for x in [10, 20, 30])
        self.assertEqual(Enumerable(gen).element_at(1), 20)
        
        gen_err = (x for x in [10])
        with self.assertRaises(IndexError):
            Enumerable(gen_err).element_at(5)

    def test_element_at_or_default_generator(self):
        gen = (x for x in [10, 20, 30])
        self.assertEqual(Enumerable(gen).element_at_or_default(1), 20)
        
        gen_def = (x for x in [10])
        self.assertIsNone(Enumerable(gen_def).element_at_or_default(5))

    def test_first_no_match(self):
        with self.assertRaises(ValueError):
            self.data.first(lambda x: x > 100)

    def test_last_no_match(self):
        with self.assertRaises(ValueError):
            self.data.last(lambda x: x > 100)


class TestQuantifiers(unittest.TestCase):
    def test_any(self):
        self.assertTrue(Enumerable([1, 2]).any())
        self.assertFalse(Enumerable([]).any())
        self.assertTrue(Enumerable([1, 2]).any(lambda x: x == 2))
        self.assertFalse(Enumerable([1, 2]).any(lambda x: x == 3))

    def test_all(self):
        self.assertTrue(Enumerable([2, 4]).all(lambda x: x % 2 == 0))
        self.assertFalse(Enumerable([2, 5]).all(lambda x: x % 2 == 0))

    def test_contains(self):
        self.assertTrue(Enumerable([1, 2]).contains(2))
        self.assertFalse(Enumerable([1, 2]).contains(3))
        
        data = [{"id": 1}, {"id": 2}]
        self.assertTrue(Enumerable(data).contains({"id": 2}, lambda x: x["id"]))

    def test_sequence_equal(self):
        self.assertTrue(Enumerable([1, 2]).sequence_equal([1, 2]))
        self.assertFalse(Enumerable([1, 2]).sequence_equal([1, 2, 3]))
        
        d1 = [{"id": 1}]
        d2 = [{"id": 1}]
        self.assertTrue(Enumerable(d1).sequence_equal(d2, lambda x: x["id"]))
    
    def test_all_empty(self):
        self.assertTrue(Enumerable([]).all(lambda x: x > 0))

    def test_sequence_equal_different_lengths(self):
        self.assertFalse(Enumerable([1, 2, 3]).sequence_equal([1, 2]))


class TestAggregates(unittest.TestCase):
    def test_count(self):
        self.assertEqual(Enumerable([1, 2, 3]).count(), 3)
        self.assertEqual(Enumerable([1, 2, 3]).count(lambda x: x > 1), 2)

    def test_max_min(self):
        e = Enumerable([1, 5, 3])
        self.assertEqual(e.max(), 5)
        self.assertEqual(e.min(), 1)
        self.assertEqual(e.max(lambda x: x * 2), 10)
        self.assertEqual(e.min(lambda x: x * 2), 2)

    def test_max_by_min_by(self):
        data = [{"id": 1, "v": 10}, {"id": 2, "v": 50}]
        e = Enumerable(data)
        self.assertEqual(e.max_by(lambda x: x["v"]), {"id": 2, "v": 50})
        self.assertEqual(e.min_by(lambda x: x["v"]), {"id": 1, "v": 10})

    def test_sum(self):
        self.assertEqual(Enumerable([1, 2, 3]).sum(), 6)
        self.assertEqual(Enumerable([{"v": 1}, {"v": 2}]).sum(lambda x: x["v"]), 3)

    def test_average(self):
        self.assertEqual(Enumerable([2, 4, 6]).average(), 4.0)
        self.assertEqual(Enumerable([{"v": 2}, {"v": 4}]).average(lambda x: x["v"]), 3.0)
        
        with self.assertRaises(ValueError):
            Enumerable([]).average()

    def test_aggregate(self):
        e = Enumerable([1, 2, 3, 4])
        self.assertEqual(e.aggregate(lambda acc, x: acc + x), 10)
        self.assertEqual(e.aggregate(lambda acc, x: acc + x, seed=10), 20)
        self.assertEqual(e.aggregate(lambda acc, x: acc + x, seed=10, result_selector=lambda x: str(x)), "20")
    
    def test_count_generator(self):
        gen = (x for x in range(5))
        self.assertEqual(Enumerable(gen).count(), 5)

    def test_max_min_empty(self):
        with self.assertRaises(ValueError):
            Enumerable([]).max()
        with self.assertRaises(ValueError):
            Enumerable([]).min()

    def test_aggregate_empty_no_seed(self):
        with self.assertRaises(TypeError):
            Enumerable([]).aggregate(lambda acc, x: acc + x)


class TestConversion(unittest.TestCase):
    def test_to_list(self):
        self.assertEqual(Enumerable((x for x in range(3))).to_list(), [0, 1, 2])

    def test_to_set(self):
        self.assertEqual(Enumerable([1, 1, 2]).to_set(), {1, 2})

    def test_to_dict(self):
        data = [{"id": 1, "val": "A"}, {"id": 2, "val": "B"}]
        res = Enumerable(data).to_dict(lambda x: x["id"], lambda x: x["val"])
        self.assertEqual(res, {1: "A", 2: "B"})
        
        data_err = [{"id": 1, "val": "A"}, {"id": 1, "val": "B"}]
        with self.assertRaises(ValueError):
            Enumerable(data_err).to_dict(lambda x: x["id"])

    def test_to_lookup(self):
        data = [{"group": 1, "val": "A"}, {"group": 1, "val": "B"}, {"group": 2, "val": "C"}]
        res = Enumerable(data).to_lookup(lambda x: x["group"], lambda x: x["val"])
        
        self.assertIn(1, res)
        self.assertEqual(res[1].to_list(), ["A", "B"])
        self.assertEqual(res[2].to_list(), ["C"])


class TestOrderedEnumerable(unittest.TestCase):
    def test_initial_sort(self):
        data = [3, 1, 2]
        oe = OrderedEnumerable(data, [(lambda x: x, False)])
        self.assertEqual(oe.to_list(), [1, 2, 3])

    def test_multiple_sort_criteria(self):
        data = [
            {"a": 1, "b": 3},
            {"a": 2, "b": 1},
            {"a": 1, "b": 2}
        ]
        oe = OrderedEnumerable(data, [(lambda x: x["a"], False)])
        oe = oe.then_by(lambda x: x["b"])
        
        self.assertEqual(oe.to_list(), [
            {"a": 1, "b": 2},
            {"a": 1, "b": 3},
            {"a": 2, "b": 1}
        ])

    def test_multiple_sort_criteria_descending(self):
        data = [
            {"a": 1, "b": 2},
            {"a": 2, "b": 1},
            {"a": 1, "b": 3}
        ]
        oe = OrderedEnumerable(data, [(lambda x: x["a"], False)])
        oe = oe.then_by_descending(lambda x: x["b"])
        
        self.assertEqual(oe.to_list(), [
            {"a": 1, "b": 3},
            {"a": 1, "b": 2},
            {"a": 2, "b": 1}
        ])


class TestGroupedEnumerable(unittest.TestCase):
    def test_grouped_enumerable_properties(self):
        ge = GroupedEnumerable("Group_A", [1, 2, 3])
        
        self.assertEqual(ge.key, "Group_A")
        self.assertEqual(ge.to_list(), [1, 2, 3])
        self.assertEqual(ge.sum(), 6)

    def test_grouped_enumerable_iteration(self):
        ge = GroupedEnumerable("Group_A", [1, 2])
        it = iter(ge)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 2)
        with self.assertRaises(StopIteration):
            next(it)


if __name__ == '__main__':
    unittest.main(verbosity=2)
