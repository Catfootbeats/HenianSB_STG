from dataclasses import dataclass


@dataclass
class GeneralConfig:
    screen_width: int
    screen_height: int
    bg_color: str
    is_full_screen: bool
    fps: int


@dataclass
class PlayerConfig:
    speed: int
    low_speed: int
    hitbox_r: int


@dataclass
class PlayerBulletConfig:
    delay: int
    speed: int
    width: int
    height: int


@dataclass
class EnemyConfig:
    health: int
    score: int


@dataclass
class EnemyBulletConfig:
    delay: int
    speed: int


@dataclass
class BossConfig:
    health: int
    score: int


@dataclass
class BossBulletConfig:
    delay: int


@dataclass
class LevelConfig:
    create_enemy_delay: int
    create_sleep: int
    create_max: int
    screen_enemy_max: int


@dataclass
class Config:
    general: GeneralConfig
    player: PlayerConfig
    enemy: EnemyConfig
    boss: BossConfig
    player_bullet: PlayerBulletConfig
    enemy_bullet: EnemyBulletConfig
    boss_bullet: BossBulletConfig
    level: LevelConfig


    def __post_init__(self):
        for section_name, section_init in self.sections():
            section = self.__dict__[section_name]
            for key, value in section.__dict__.items():
                self.__dict__[f"{section_name}_{key}"] = value


    @staticmethod
    def sections() -> list[tuple[str, callable]]:
        return [(k, v) for k, v in Config.__annotations__.items() if v.__name__.endswith("Config")]
    

    @staticmethod
    def non_sections() -> list[str]:
        return [k for k, v in Config.__annotations__.items() if not v.__name__.endswith("Config")]


    @staticmethod
    def default() -> 'Config':
           return Config(
                general=GeneralConfig(
                    screen_width=1280,
                    screen_height=768,
                    bg_color='#66ccff',
                    is_full_screen=False,
                    fps=60
                ),
                player=PlayerConfig(
                    speed=9,
                    low_speed=3,
                    hitbox_r=5
                ),
                player_bullet=PlayerBulletConfig(
                    delay=2,
                    speed=15,
                    width=10,
                    height=10,
                ),
                enemy=EnemyConfig(
                    health=1,
                    score=1000,
                ),
                enemy_bullet=EnemyBulletConfig(
                    delay=1,
                    speed=15,
                ),
                boss=BossConfig(
                    health=1,
                    score=100,
                ),
                boss_bullet=BossBulletConfig(
                    delay=100,
                ),
                level=LevelConfig(
                    create_enemy_delay=100,
                    create_sleep=500,
                    create_max=10,
                    screen_enemy_max=10,
                )
            )


    @staticmethod
    def from_dict(config_dict: dict) -> 'Config':
        for section_name, section_init in Config.sections():
            config_dict[section_name] = section_init(**config_dict[section_name])
        return Config(**config_dict)
    

    def to_dict(self) -> dict:
        result = {}
        for section_name, section_init in self.sections():
            result[section_name] = self.__dict__[section_name].__dict__
        for field in self.non_sections():
            result[field] = self.__dict__[field]
        return result


def load_config() -> Config:
    import os
    import sys
    import toml
    import platform
    from os import path
    from stg import __is_pyinstaller__, __is_macos_appbundle__, debug, msgbox
    
    class FirstTimeRunMacOSAppError(Exception):
        pass

    # 确定配置文件路径
    if __is_pyinstaller__:
        config_path = path.abspath(path.join(path.dirname(sys.executable), "config.toml"))
        if __is_macos_appbundle__:
            debug("Running on macOS, using config file in parent directory.")
            config_path = path.abspath(path.join(
                os.getenv("HOME"),
                "Library/Preferences/dev.luotianyi.pygame.beating-agent-v/config.toml"
            ))
            os.makedirs(path.dirname(config_path), exist_ok=True)
    else:
        config_path = path.abspath(path.join(path.dirname(__file__), "../../config.toml"))

    # 读取或创建配置文件
    if not path.exists(config_path):
        debug("Config file not found, using default config.")
        debug(f"Writing default config to file: {config_path}")
        try:
            with open(config_path, "w+", encoding="utf-8") as f:
                toml.dump(Config.default().to_dict(), f)
            if __is_macos_appbundle__:
                raise FirstTimeRunMacOSAppError
            return Config.default()
        except IOError:
            msgbox(f"配置文件 {config_path} 不可写入，请调整权限后重试。")
        except FirstTimeRunMacOSAppError:
            msgbox(f"您似乎是首次在 macOS 上运行本游戏，由于 Apple 对应用程序完整性的检查，"
                   f"游戏配置文件已保存在 {config_path}。"
                   f"此通知不是错误，仅在您首次运行游戏时显示一次。")
    else:
        debug(f"Loading config from file: {config_path}")
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                return Config.from_dict(toml.load(f))
        except IOError:
            msgbox(f"配置文件 {config_path} 不可读取，请调整权限后重试。")
        except toml.TomlDecodeError:
            msgbox(f"配置文件 {config_path} 格式错误，请检查后重试。")
