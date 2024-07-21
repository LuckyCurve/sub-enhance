import adaptor.inbounds.service_controller as service_controller


def test_hide_actual_host():
    res = service_controller.hide_actual_host(
        "https://www.google.com?url=www.luckycurve.xyz", ["www.luckycurve.xyz"]
    )

    assert res == "https://www.google.com?url=www.encode0.com"


def test_replace_with_actual_host():
    res = service_controller.replace_with_actual_host(
        "https://www.google.com?url=www.encode0.com", ["www.luckycurve.xyz"]
    )

    assert res == "https://www.google.com?url=www.luckycurve.xyz"
