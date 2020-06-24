from src.config.schemas import DivisorConfig

configs = {
    "REINVENT_2018": DivisorConfig(
        narrow_gradient_threshold=0.125,
        wide_gradient_threshold=0.3,
        use_wide_gradient=True,
        distance_threshold=0.1,
        pre_corner_range=2,
        post_corner_range=1
    ),
    "FUMIAKI_LOOP_2020": DivisorConfig(
        narrow_gradient_threshold=0.15,
        wide_gradient_threshold=0.5,
        use_wide_gradient=True,
        distance_threshold=0.02,
        pre_corner_range=5,
        post_corner_range=5
    )
}
