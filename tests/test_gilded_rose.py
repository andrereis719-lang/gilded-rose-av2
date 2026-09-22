from gilded_rose import Item, GildedRose


def test_item_normal_antes_do_vencimento():
    item = Item("Elixir of the Mongoose", 5, 10)

    GildedRose([item]).att()

    assert item.sell_in == 4
    assert item.quality == 9


def test_item_normal_apos_o_vencimento():
    item = Item("Elixir of the Mongoose", 0, 10)

    GildedRose([item]).att()

    assert item.sell_in == -1
    assert item.quality == 8


def test_aged_brie_aumenta_qualidade():
    item = Item("Aged Brie", 5, 10)

    GildedRose([item]).att()

    assert item.sell_in == 4
    assert item.quality == 11


def test_aged_brie_apos_vencimento():
    item = Item("Aged Brie", 0, 10)

    GildedRose([item]).att()

    assert item.sell_in == -1
    assert item.quality == 12


def test_sulfuras_nao_muda():
    item = Item("Sulfuras, Hand of Ragnaros", 10, 80)

    GildedRose([item]).att()

    assert item.sell_in == 10
    assert item.quality == 80


def test_backstage_mais_de_dez_dias():
    item = Item(
        "Backstage passes to a TAFKAL80ETC concert",
        15,
        10
    )

    GildedRose([item]).att()

    assert item.sell_in == 14
    assert item.quality == 11


def test_backstage_entre_seis_e_dez_dias():
    item = Item(
        "Backstage passes to a TAFKAL80ETC concert",
        10,
        10
    )

    GildedRose([item]).att()

    assert item.sell_in == 9
    assert item.quality == 12


def test_backstage_entre_um_e_cinco_dias():
    item = Item(
        "Backstage passes to a TAFKAL80ETC concert",
        5,
        10
    )

    GildedRose([item]).att()

    assert item.sell_in == 4
    assert item.quality == 13


def test_backstage_apos_o_show():
    item = Item(
        "Backstage passes to a TAFKAL80ETC concert",
        0,
        40
    )

    GildedRose([item]).att()

    assert item.sell_in == -1
    assert item.quality == 0
