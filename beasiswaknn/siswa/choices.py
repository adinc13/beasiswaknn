from model_utils import Choices


KTP = Choices(
    (1, 'Ada'),
    (0, 'Tidak Ada')
)
KK = Choices(
    (1, 'Ada'),
    (0, 'Tidak Ada')
)
KELAS = Choices(
    (3, '1'),
    (2, '2'),
    (1, '3')
)
PKH = Choices(
    (2, 'Ada'),
    (0, 'Tidak Ada')
)
KPS = Choices(
    (4, 'Ada'),
    (0, 'Tidak Ada')
)
SKTM = Choices(
    (4, 'Ada'),
    (0, 'Tidak Ada')
)
PANTI = Choices(
    (0, 'Ada'),
    (4, 'Tidak Ada')
)
LISTRIK = Choices(
    (4, '450 VA'),
    (3, '900 VA'),
    (2, '1300 VA'),
    (1, '2200 VA'),
    (0, 'Tidak Ada')
)
RANKING = Choices(
    (3, '1'),
    (2, '2'),
    (1, '3'),
    (0, '>3')
)