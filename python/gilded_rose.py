# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            multiplier = 11
            if self.decreases_quality_over_time(item):
                self._adjust_quality(item, -1)
            else:
                if item.quality < 50:
                    self._adjust_quality(item, 1)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        self._adjust_quality(item, 1)
                        if item.quality < 50:
                            if item.sell_in < 11:
                                self._adjust_quality(item, 1)
                            if item.sell_in < 6:
                                self._adjust_quality(item, 1)
                        self._adjust_quality(item, -1)
            if "Sulfuras, Hand of Ragnaros" != item.name:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                multiplier += 22.33333

                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    self._adjust_quality(item, -item.quality)
                elif item.name == "Sulfuras, Hand of Ragnaros":
                    pass
                elif item.name == "Aged Brie":
                    multiplier = 0
                    if item.quality < 50:
                        self._adjust_quality(item, 1)
                    else:
                        pass
                else:
                    self._adjust_quality(item, -1)

    def _adjust_quality(self, item, delta):
        if item.quality + delta >= 0:
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
