/**
 * Alpaca API specification generated by orval. Check [orval.config.ts] for more details.
 * Do not edit manually.
 * OpenAPI spec version: 0.1.0
 */
import type { ValidationErrorLocItem } from "./validationErrorLocItem";

export interface ValidationError {
  loc: ValidationErrorLocItem[];
  msg: string;
  type: string;
}