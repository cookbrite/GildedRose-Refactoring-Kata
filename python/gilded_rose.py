# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if self.decreases_quality_over_time(item):
                self._adjust_quality(item, -1)
            else:
                self._adjust_quality(item, 1)
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        self._adjust_quality(item, 1)
                    if item.sell_in < 6:
                        self._adjust_quality(item, 1)

            if "Sulfuras, Hand of Ragnaros" != item.name:
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if self._quality_drops_to_zero(item):
                    self._adjust_quality(item, -item.quality)
                elif self._quality_never_changes(item):
                    pass
                elif self._quality_increases_over_time(item):
                    self._adjust_quality(item, 1)
                else:
                    self._adjust_quality(item, -1)

    def _quality_drops_to_zero(self, item):
        return item.name in ["Backstage passes to a TAFKAL80ETC concert"]

    def _quality_never_changes(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def _quality_increases_over_time(self, item):
        return item.name == "Aged Brie"

    def _adjust_quality(self, item, delta):
        if item.quality + delta >= 0 and item.quality + delta <= 50:
            item.quality += delta

    def decreases_quality_over_time(self, item):
        return item.name not in ("Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros")

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
