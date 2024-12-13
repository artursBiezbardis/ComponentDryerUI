import GLOBALS as glob_val


class AsyncQueueUtilities:

    @staticmethod
    def add_item_to_queue(async_queue: list):
        new_key = 0
        new_queue = async_queue.copy()

        if async_queue:
            last_async_key = async_queue[-1]
            new_key = last_async_key + 1
        new_queue.append(new_key)
        glob_val.global_async_db_queue = new_queue
        print(new_queue)
        return new_queue

