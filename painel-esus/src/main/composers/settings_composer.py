from src.presentations.controllers.settings.settings_controller import (
    SettingsController,
)


def settings_factory():
    return SettingsController()


def instalation_status_composer():
    return settings_factory().instalation_status


def check_instalation_composer():
    return settings_factory().check_instalation


def test_connection_composer():
    return settings_factory().test_connection


def save_instalation_settings_composer():
    return settings_factory().save_instalation_settings


def get_term_acceptance_settings_composer():
    return settings_factory().get_term_acceptance_settings


def save_term_acceptance_settings_composer():
    return settings_factory().save_term_acceptance_settings


def stop_instalation_settings_composer():
    return settings_factory().stop_instalation_settings


def start_instalation_composer():
    return settings_factory().start_instalation


def instalation_ready_composer():
    return settings_factory().instalation_ready
