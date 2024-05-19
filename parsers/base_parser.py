from abc import ABC, abstractmethod
from utils.wechat import WeChatNotifier
import json


class BaseParser(ABC):
    @abstractmethod
    def parse(self, html):
        pass

    # @abstractmethod
    def send_notification(self, new_litters):
        wechat_notifier = WeChatNotifier()
        wechat_notifier.send_wechat_notification(
            self.name, self.url, new_litters)

    # Display the litters >> Debugging purpose
    def display_litter(self):
        for litter in self.litters:
            print(litter)

    # Check if the litters have changed
    def find_data_changes(self):
        # get the litters from the storage file
        if self.storage_path.exists():
            with open(self.storage_path, "r", encoding="utf-8") as f:
                previous_litters = json.load(f)
        else:
            previous_litters = []

        # save the current litters to the storage file
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump([litter.to_dict() for litter in self.litters],
                      f, ensure_ascii=False, indent=4, default=str)

        # compare the current litters with the previous ones
        current_litters = [litter.to_dict() for litter in self.litters]
        if current_litters != previous_litters:
            new_litters = []
            for litter in current_litters:
                if litter not in previous_litters:
                    new_litters.append(litter)
            return new_litters
        else:
            return False
