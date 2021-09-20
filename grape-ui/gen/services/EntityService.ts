/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import { request as __request } from '../core/request';

export class EntityService {

    /**
     * return all classes from all modules with methods
     * @returns any Success
     * @throws ApiError
     */
    public static async getClasses(): Promise<any> {
        const result = await __request({
            method: 'GET',
            path: `/entity/class`,
        });
        return result.body;
    }

    /**
     * return a very specific class with much detail about its methods
     * @param classId The class identifier
     * @returns any Success
     * @throws ApiError
     */
    public static async getClassController(
        classId: string,
    ): Promise<any> {
        const result = await __request({
            method: 'GET',
            path: `/entity/class/${classId}`,
        });
        return result.body;
    }

    /**
     * Get all methods
     * @returns any Success
     * @throws ApiError
     */
    public static async getMethodControllerList(): Promise<any> {
        const result = await __request({
            method: 'GET',
            path: `/entity/method`,
        });
        return result.body;
    }

    /**
     * Get a method by method id from a particular version
     * @param versionId The id of the version
     * @param methodId The id of the method
     * @returns any Success
     * @throws ApiError
     */
    public static async getMethodController(
        versionId: string,
        methodId: string,
    ): Promise<any> {
        const result = await __request({
            method: 'GET',
            path: `/entity/method/${methodId}/${versionId}`,
        });
        return result.body;
    }

    /**
     * return all modules
     * @returns any Success
     * @throws ApiError
     */
    public static async getModuleController(): Promise<any> {
        const result = await __request({
            method: 'GET',
            path: `/entity/module`,
        });
        return result.body;
    }

    /**
     * return all versions
     * @returns any Success
     * @throws ApiError
     */
    public static async getMethodController1(): Promise<any> {
        const result = await __request({
            method: 'GET',
            path: `/entity/version`,
        });
        return result.body;
    }

}