from typing import Iterable

from linqex import Enumerable

class LogProcessor:
    """
    Processes massive log streams using deferred execution and chunking.
    Demonstrates how to process data without loading the entire stream into RAM ($O(1)$ memory).
    """

    @staticmethod
    def simulate_log_stream() -> Iterable[str]:
        """A generator simulating a continuous stream of server logs."""
        logs = [
            "INFO: Server started",
            "ERROR: DB Connection failed [Timeout]",
            "INFO: User logged in",
            "WARN: High memory usage",
            "ERROR: Null Reference Exception",
            "INFO: Health check OK",
            "ERROR: Invalid credentials"
        ]
        # In reality, this could yield line-by-line from a 100GB text file.
        for log in logs:
            yield log

    def process_critical_errors_in_batches(self, batch_size: int = 2):
        """
        Filters out critical errors, chunks them into batches, and simulates 
        sending them to an external monitoring service.
        """
        log_stream = Enumerable(self.simulate_log_stream())

        error_batches = (log_stream
            # 1. Filter: Only keep lines starting with ERROR
            .where(lambda line: line.startswith("ERROR"))
            
            # 2. Transform: Extract just the message payload
            .select(lambda line: line.split(": ", 1)[1])
            
            # 3. Chunk: Group into lists of specific size for bulk database inserts
            .chunk(batch_size))

        # The stream is NOT executed until this for-loop pulls the chunks
        for i, batch in enumerate(error_batches, 1):
            print(f"Sending Batch #{i} to DataDog / NewRelic:")
            for error_msg in batch:
                print(f"  -> {error_msg}")
            print("-" * 30)

if __name__ == "__main__":
    processor = LogProcessor()
    processor.process_critical_errors_in_batches(batch_size=2)
